import boto3

# Replace with your actual SQS Queue URL
QUEUE_URL = "https://sqs.region.amazonaws.com/123456789012/queue_name"


def add_message_to_sqs():
    message_body = "X" * 1024 * 1024  # 1 MB

    sqs = boto3.client("sqs")
    response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=message_body,
        # MessageAttributes={
        #     "Attr001": {"StringValue": "System", "DataType": "String"},
        #     "Attr002": {"StringValue": "100", "DataType": "Number"},
        # },
    )

    print(f"Message sent with ID: {response['MessageId']}")


if __name__ == "__main__":
    add_message_to_sqs()
