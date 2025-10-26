import aws_cdk as core
import aws_cdk.assertions as assertions

from sqs_to_lambda.sqs_to_lambda_stack import SqsToLambdaStack

# example tests. To run these tests, uncomment this file along with the example
# resource in sqs_to_lambda/sqs_to_lambda_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SqsToLambdaStack(app, "sqs-to-lambda")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
