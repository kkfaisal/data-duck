import time
import boto3
import logging

amplit_table_ddl = """
CREATE EXTERNAL TABLE {event_name}(
  `data` string)
PARTITIONED BY ( 
  `partn_date` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://<s3_bucket>/{event_name}/dev/app_launched/export_id=xxxx'
TBLPROPERTIES (
  'projection.enabled'='true', 
  'projection.partn_date.format'='yyyyMMdd', 
  'projection.partn_date.range'='NOW-1YEARS,NOW', 
  'projection.partn_date.type'='date', 
  'storage.location.template'='s3://<s3_bucket>/{event_name}/dev/app_launched/export_id=xxxxx/${{partn_date}}/', 
  'transient_lastDdlTime'='1706003050')

"""

def create_amplitude_event_table(event_name, create_view):
    """
    Create an Amplitude event table based on the provided parameters.
    
    :param ampli_src: The source of the Amplitude data (e.g., 'Website', 'Mobile App').
    :param event_name: The name of the event to be created.
    :param create_view: Whether to create a flattened view of the data ('Yes' or 'No').
    """
    # Substitute the event_name placeholder in the DDL
    ddl_with_event_name = amplit_table_ddl.format(event_name=event_name)
    time.sleep(1)  # Simulate time taken to create the table
    yield f"Creating Amplitude event table with DDL: {ddl_with_event_name}"
    time.sleep(2)  # Simulate time taken to create the table
    yield f"Amplitude event table '{event_name}' created successfully."

    if create_view == 'Yes':
        yield f"Creating a flattened view for the event: {event_name}"
        time
        yield "TODO :Flattened view SQL"
    else:
        yield f"No flattened view will be created for the event: {event_name}"

    final_result = f"Amplitude event table '{event_name}' created successfully."   
    yield ("result", final_result)



