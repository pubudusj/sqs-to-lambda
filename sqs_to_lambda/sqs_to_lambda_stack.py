from aws_cdk import (
    CfnOutput,
    Stack,
    aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_lambda_event_sources as lambda_event_sources,
)
from constructs import Construct


class SqsToLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # example resource
        queue = sqs.Queue(
            self,
            "SqsToLambdaQueue",
            dead_letter_queue=sqs.DeadLetterQueue(
                max_receive_count=1,
                queue=sqs.Queue(
                    self,
                    "SqsToLambdaDeadLetterQueue",
                ),
            ),
        )

        # create a lambda function and set up SQS as an event source
        function = _lambda.Function(
            self,
            "SqsToLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_13,
            handler="index.handler",
            code=_lambda.Code.from_asset("lambda"),
        )

        function.add_event_source(lambda_event_sources.SqsEventSource(queue))

        # Output
        CfnOutput(
            self,
            "QueueURL",
            value=queue.queue_url,
            description="The URL of the SQS Queue",
        )
