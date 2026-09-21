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
                        "cd Ayesha/", 
                        "pip install -r requirements.txt",
                        "cdk synth"
                    ],
                primary_output_directory = "Ayesha/cdk.out"               
            )

        MyPipeline = pipelines_.CodePipeline(self,
                id = "pipeline",
                synth = synth
        )

        alphaStage = PipelineStage(self, "Alpha")
        MyPipeline.add_stage(alphaStage,
            pre = [pipelines_.ShellStep(
                        id = "Unit Tests",
                        commands=[  "npm install -g aws-cdk",
                                    "cd Ayesha/",
                                    "pip install -r requirements.txt",
                                    "pip install pytest", 
                                    "python3 -m pytest"
                                ]
                    )]
                )

        # betaStage = PipelineStage(self, "Beta")
        # MyPipeline.add_stage(betaStage,
        #     post = [pipelines.ShellStep(id = "Functional Tests",
        #     commands=[]
        #     ]
        # )
        
        # gemmaStage = PipelineStage(self, "Gemma")
        # MyPipeline.add_stage(gemmaStage,
        #     post = [pipelines.ShellStep(id = "Integration Tests",
        #     commands=[]
        #     ]
        # )

        # prodStage = PipelineStage(self, "Prod")
        # MyPipeline.add_stage(prodStage,
        #     pre=[pipelines.ManualApprovalStep("PromoteToProd",
        #     # All options below are optional
        #     comment="Please validate changes",
        #     )]
        # )