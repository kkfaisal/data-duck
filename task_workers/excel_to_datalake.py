import time

def excel_to_datalake(file_path):
    yield f"Starting upload of Excel file: {file_path}"
    # Simulate upload progress
    for i in range(1, 4):
        time.sleep(1)
        yield f"Uploading... step {i}/3"
    # Read the first line of the uploaded file
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
    except Exception as e:
        first_line = f"Error reading file: {e}"
    yield ("Success", f"First line of file: {first_line}")
