from aws_cdk import (
    Stack,
    pipelines as pipelines_,
    SecretValue,
    aws_codepipeline_actions,
    Stage
)

from constructs import Construct
from ayesha.pipeline_stage import PipelineStage

class PipelineStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        source = pipelines_.CodePipelineSource.git_hub(
                repo_string = "AyeshaOmer/ProjectName", 
                branch = "main",
                authentication = SecretValue.secrets_manager("githubSecret"),
                trigger = aws_codepipeline_actions.GitHubTrigger("POLL")
            )
        
        synth=pipelines_.ShellStep(
                id = "Synth",
                input = source,
                commands = [
                        "npm install -g aws-cdk", 
                        " cd Ayesha/", 
                        "pip install -r requirements.txt",
                        "cdk synth"
                    ],
                primary_output_directory = "Ayesha/cdk.out"               
            )

        pipeline = pipelines_.CodePipeline(self,
                id = "pipeline",
                synth = synth
        )

        alphaStage = PipelineStage(self, "Alpha")
        pipeline.add_stage(alphaStage,
            post = []
        )