def get_task_parameters(task_id):
    # Example parameters for different tasks
    task_parameters = {
        'Create Amplitude Event Table': [
            {'name': 'ampli_src', 'type': 'select', 'label': 'Amplitude Source', 'options': ['Website', 'Mobile App']},
            {'name': 'event_name', 'type': 'text', 'label': 'Event Name'},
            {'name': 'create_view', 'type': 'select', 'label': 'Create Faltten View?', 'options': ['Yes', 'No']},
        ],
        'Excel to Data Lake': [
            {'name': 'excel_file', 'type': 'file', 'label': 'Upload Excel File'},
        ],
        '1.2': [
            {'name': 'param1', 'type': 'select', 'label': 'Parameter 1', 'options': ['Choice A', 'Choice B']},
            {'name': 'param2', 'type': 'text', 'label': 'Parameter 2'}
        ],
        '2.1': [
            {'name': 'param1', 'type': 'select', 'label': 'Parameter 1', 'options': ['True', 'False']},
            {'name': 'param2', 'type': 'select', 'label': 'Parameter 2', 'options': ['Yes', 'No']}
        ],
        '1.3': [
            {'name': 'param1', 'type': 'file', 'label': 'Upload File'}
        ],
        # Add more tasks and their parameters as needed
    }
    
    return task_parameters.get(task_id, [])

# Example usage
if __name__ == '__main__':
    task_id = '1.1'
    parameters = get_task_parameters(task_id)
    print(f"Parameters for task {task_id}: {parameters}")
