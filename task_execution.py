import time
import json  # Import json module to safely pass strings to JavaScript
from task_workers.test import sample_task_worker  # Import the sample task worker

def execute_task_1_1(params):
    yield f"Starting execution of task 1.1 with parameters: {params}"
    
    # Call the sample task worker and stream its logs
    final_result = None
    for worker_log in sample_task_worker(params):
        if isinstance(worker_log, tuple) and worker_log[0] == "result":
            final_result = worker_log[1]
        else:
            yield worker_log

    # Simulate task execution with logs
    for i in range(10):
        log_entry = f"Log entry {i+1}: Executing step {i+1} with parameters {params}"
        yield log_entry
        time.sleep(.5)  # Simulate time taken for each step

    # Simulate task success or failure
    task_success = True  # Change this to False to simulate failure
    if task_success:
        yield "Task execution completed successfully."
        status = "Success"
    else:
        yield "Task execution failed."
        status = "Failure"

    yield status, final_result or "Final output from task 1.1"

def execute_task_1_2(params):
    yield f"Starting execution of task 1.2 with parameters: {params}"

    # Simulate task execution with logs
    for i in range(5):
        log_entry = f"Log entry {i+1}: Executing step {i+1} with parameters {params}"
        yield log_entry
        time.sleep(1)  # Simulate time taken for each step

    # Simulate task success or failure
    task_success = False  # Set to False to simulate failure after 5th step
    if task_success:
        yield "Task execution completed successfully."
        status = "Success"
    else:
        yield "Task execution failed."
        status = "Failure"

    yield status, "Final output from task 1.2"

def execute_task_1_3(params):
    yield f"Starting execution of task 1.3 with parameters: {params}"

    # Simulate task execution with logs
    for i in range(7):
        log_entry = f"Log entry {i+1}: Executing step {i+1} with parameters {params}"
        yield log_entry
        time.sleep(1)  # Simulate time taken for each step

    # Simulate task success or failure
    task_success = True  # Change this to False to simulate failure
    if task_success:
        yield "Task execution completed successfully."
        status = "Success"
    else:
        yield "Task execution failed."
        status = "Failure"

    yield status, "Final output from task 1.3"

# Add more task-specific functions as needed

def stream_task_execution(task_id, params):
    task_functions = {
        'Create Amplitude Event Table': execute_task_1_1,
        '1.2': execute_task_1_2,
        '1.3': execute_task_1_3,
        # Add more task mappings as needed
    }

    if task_id in task_functions:
        try:
            for log in task_functions[task_id](params):
                yield log
        except Exception as e:
            yield f"Exception occurred: {str(e)}"
            # Yield a tuple to mark status as Failure and carry final output
            yield ("Failure", f"Exception: {str(e)}")
    else:
        yield f'Task ID {task_id} not recognized.'
        yield ("Failure", "")
