from flask import Flask, render_template, request, redirect, url_for, session, Response, stream_with_context, send_from_directory, jsonify
import os
import yaml  # Import yaml module to load task list from a YAML file
from task_parameters import get_task_parameters
from task_execution import stream_task_execution  # Import the new function
import html  # Import html module to escape logs
import json  # Import json module to safely pass strings to JavaScript
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Add a secret key for session management

# Hardcoded credentials
USERNAME = 'admin'
PASSWORD = 'password'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@login_required
def home():
    return redirect(url_for('tasks'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True  # Set session variable
            return redirect(url_for('tasks'))  # Redirect to tasks page
        else:
            return "Invalid credentials, please try again."
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)  # Clear session variable
    return redirect(url_for('login'))

@app.route('/tasks')
@login_required
def tasks():
    # Load task categories and tasks from a YAML file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    yaml_file_path = os.path.join(script_dir, 'task_list.yaml')
    with open(yaml_file_path, 'r') as file:
        task_categories = yaml.safe_load(file)
    
    return render_template('tasks.html', task_categories=task_categories)

@app.route('/task/<task_id>', methods=['GET', 'POST'])
@login_required
def task(task_id):
    if request.method == 'POST':
        parameters = get_task_parameters(task_id)
        params = {}
        for param in parameters:
            if param['type'] == 'file':
                file = request.files[param['name']]
                if file:
                    # Ensure the 'uploads' directory exists in the script's directory
                    script_dir = os.path.dirname(os.path.abspath(__file__))
                    uploads_dir = os.path.join(script_dir, 'uploads')
                    if not os.path.exists(uploads_dir):
                        os.makedirs(uploads_dir)
                    file_path = os.path.join(uploads_dir, file.filename)
                    file.save(file_path)
                    params[param['name']] = file_path
            else:
                params[param['name']] = request.form[param['name']]
        return redirect(url_for('execute_task', task_id=task_id, **params))
    
    parameters = get_task_parameters(task_id)  # Get parameters for the task
    return render_template('task.html', task_id=task_id, parameters=parameters)

@app.route('/execute_task/<task_id>')
@login_required
def execute_task(task_id):
    parameters = get_task_parameters(task_id)
    params = {param['name']: request.args.get(param['name']) for param in parameters}
    return Response(stream_with_context(execute_task_stream(task_id, params)), mimetype='text/html')

@app.route('/get_logs/<task_id>')
@login_required
def get_logs(task_id):
    # Get logs from session, initialize if not present
    task_results = session.get('task_results', {'logs': [], 'status': None, 'final_output': None})
    return jsonify(
        logs=task_results.get('logs', []),
        status=task_results.get('status'),
        final_output=task_results.get('final_output')
    )

def execute_task_stream(task_id, params):
    # Initialize task results in session
    session['task_results'] = {'logs': [], 'status': None, 'final_output': None}
    
    yield render_template('execute_task_start.html', task_id=task_id, params=params).encode('utf-8')
    
    for log in stream_task_execution(task_id, params):
        if isinstance(log, tuple):
            status, final_output = log
            # Update session with final status and output
            session['task_results']['status'] = status
            session['task_results']['final_output'] = final_output
            session.modified = True
            if status == "Success":
                yield "<script>updateStatus(true);</script>".encode('utf-8')
            else:
                yield "<script>updateStatus(false);</script>".encode('utf-8')
            # Immediately update the Final Output text area
            yield f"<script>document.getElementById('final-output').value = {json.dumps(final_output)};</script>".encode('utf-8')
        else:
            # Append log to session
            session['task_results']['logs'].append(log)
            session.modified = True
            yield f"<script>appendLog({json.dumps(log)});</script>".encode('utf-8')

@app.route('/static/<path:path>')
@login_required
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change the port to 5001
