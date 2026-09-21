from aws_cdk import (
    Stage
)

from constructs import Construct

from ayesha.ayesha_stack import AyeshaStack

class PipelineStage(Stage):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        APPStack = AyeshaStack(self, "id")