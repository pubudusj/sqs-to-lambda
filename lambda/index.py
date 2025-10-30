def handler(event, context):
    for record in event["Records"]:
        # print message body size in kB
        body_size_kb = len(record["body"]) / 1024
        print(f"Message Body Size: {body_size_kb:.2f} kB")
