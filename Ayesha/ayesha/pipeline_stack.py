from aws_cdk import (
    Stack,
    SecretValue,
    pipelines as pipelines,
    aws_secretsmanager as secretsmanager,
    aws_codepipeline_actions as actions,
)
from constructs import Construct

class MyPipelineStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

    # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.pipelines/CodePipelineSource.html
    # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk/SecretValue.html
    # https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/create-secret.html
    source = pipelines.CodePipelineSource.git_hub(
            repo_string = "AyeshaOmer/WSU2026", 
            branch = "main",
            authentication = SecretValue.secrets_manager("githubSecret"),
            trigger =actions.GitHubTrigger("POLL"))
    
    
    codeBuild = pipelines.ShellStep("synth", 
        commands = ["cd ProjectName/Ayesha/", "pip install requirements.txt", "cdk synth"],
        input = source,
        primary_output_directory = "ProjectName/Ayesha/cdk.out")

    appPipeline = pipelines.CodePipeline()

