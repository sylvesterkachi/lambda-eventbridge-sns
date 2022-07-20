import json
import boto3, random
from datetime import datetime

client = boto3.client('events')

def lambda_handler(event, context):
    # TODO implement
    sources = ["atm.bluebank.events", "bankbranch.bluebank.events"]
    bank_source = str(random.choice(sources))
    t_datetime = datetime.today().strftime('%m/%d/%Y, %H:%M:%S')

    response = client.put_events(
    Entries=[
        {       "Source": bank_source,
                "Resources": [
                "arn:aws:events:us-east-1:185131372497:event-bus/bluebank-bus",
            ],
                "DetailType": "BOP transaction",
                "Time": datetime.today().strftime('%Y-%m-%d'),
                "Detail": "{ \"transaction_value\": \"10,800\", \"date\": \""+t_datetime+"\",  \"customer\": \"Joe Simon\", \"bop_reportable\": \"Yes\" }",
            "EventBusName": "arn:aws:events:us-east-1:185131372497:event-bus/bluebank-bus",
            "TraceHeader": "atmORbanklocation"
        },
    ],
)
    print(response)

    return {
        'statusCode': 200,
        'body': json.dumps('Event Unterwegs!')
    }
