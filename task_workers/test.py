import time
def sample_task_worker(params):
    yield "Starting sample task worker..."
    for i in range(3):
        time.sleep(1)
        log_entry = f"Sample task worker: Step {i+1} with parameters {params}"
        yield log_entry
    yield "Sample task worker completed."
    final_result = "Final result from sample task worker"
    # raise "This is an error message"
    yield ("result", final_result)
