import time
import json  # Import json module to safely pass strings to JavaScript
from task_workers.test import sample_task_worker  # Import the sample task worker
from task_workers.amplitude_table_create import create_amplitude_event_table  # Import the function to create Amplitude event table

def execute_task_function(params,task_fun):
    yield f"Starting execution of task with parameters: {params}"
    
    # Call the sample task worker and stream its logs
    final_result = None
    for worker_log in task_fun(params['event_name'], params['create_view']):
        if isinstance(worker_log, tuple) and worker_log[0] == "result":
            final_result = worker_log[1]
        else:
            yield worker_log
    # Simulate task success or failure
    task_success = True  # Change this to False to simulate failure
    if task_success:
        yield "Task execution completed successfully."
        status = "Success"
    else:
        yield "Task execution failed."
        status = "Failure"

    yield status, final_result or "Final output from task 1.1"


def stream_task_execution(task_id, params):
    task_functions = {
        'Create Amplitude Event Table': create_amplitude_event_table
        # Add more task mappings as needed
    }

    if task_id in task_functions:
        try:
            # Pass task_fun first, then params
            for log in execute_task_function(params, task_functions[task_id]):
                yield log
        except Exception as e:
            yield f"Exception occurred: {str(e)}"
            # Yield a tuple to mark status as Failure and carry final output
            yield ("Failure", f"Exception: {str(e)}")
    else:
        yield f'Task ID {task_id} not recognized.'
        yield ("Failure", "")
