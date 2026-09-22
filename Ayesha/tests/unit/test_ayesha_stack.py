import aws_cdk as core
import aws_cdk.assertions as assertions

from ayesha.ayesha_stack import AyeshaStack

# example tests. To run these tests, uncomment this file along with the example
# resource in ayesha/ayesha_stack.py
def test_lambda_created():
    app = core.App()
    stack = AyeshaStack(app, "ayesha")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::Lambda::Function", 2)
