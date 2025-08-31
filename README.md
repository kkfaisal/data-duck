

# 🦆 Data-Duck

Welcome to **Data-Duck** – the quackiest way to run Python functions from a web UI! 🦆💻

Data-Duck is a web-based tool that lets you create, run, and monitor Python functions (tasks) with the grace of a duck gliding across a pond. No more command-line flapping – just click, upload, and watch your code take flight!

---

## 🛠️ How to Add a New Python Function (Task) to the UI

1. **Write Your Python Function:**
   - Waddle over to the `task_workers/` folder.
   - Create a new `.py` file or add your function to an existing one.
   - Your function should be a generator (it should `yield` progress updates, because ducks like to keep you posted).

   Example:
   ```python
   def my_cool_task(param1, param2):
       yield f"Starting with {param1} and {param2}!"
       # ...do stuff...
       yield ("Success", "All done! 🦆")
   ```

2. **Register Your Function in `task_execution.py`:**
   - Open `task_execution.py`.
   - Add your function to the `task_functions` dictionary in `stream_task_execution`.
   - Example:
     ```python
     from task_workers.my_worker import my_cool_task
     task_functions = {
         'My Cool Task': my_cool_task,
         # ...other tasks...
     }
     ```

3. **Add Task Parameters in `task_parameters.py`:**
   - Open `task_parameters.py`.
   - Add an entry for your task in the `task_parameters` dictionary.
   - Example:
     ```python
     'My Cool Task': [
         {'name': 'param1', 'type': 'text', 'label': 'Parameter 1'},
         {'name': 'param2', 'type': 'text', 'label': 'Parameter 2'},
     ],
     ```

4. **Add Your Task to the YAML File:**
   - Open `task_list.yaml`.
   - Add your task under the appropriate category.
   - Example:
     ```yaml
     My Category:
       - id: 'My Cool Task'
         name: 'My Cool Task'
         description: 'Does something really cool!'
     ```

5. **Restart the App:**
   - Give your feathers a shake and restart the Flask app. Your new task will appear in the UI, ready to quack!

---

## 📝 Editing the YAML File
- The `task_list.yaml` file is where you organize your tasks into categories.
- Each task needs an `id`, `name`, and `description`.
- Don’t forget: YAML is picky about spaces. Ducks are not, but YAML is.

---

## 🦆 Why Data-Duck?
- Because ducks are awesome.
- Because web UIs are easier than command lines.
- Because you deserve to have fun while running Python code.

---

## 💡 Pro Tips
- If you see an error, don’t panic – just keep calm and quack on.
- Want to add a file upload? Set the parameter type to `file` in `task_parameters.py`.
- Ducks love progress bars. Make your function yield lots of updates!

