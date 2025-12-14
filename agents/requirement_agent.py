from autogen_agentchat.agents import AssistantAgent
from models import model

requirement_agent = AssistantAgent(
    name="RequirementAgent",
    model_client=model,
    system_message="""
        Convert user input into structured software requirements (python language).:
        - Functional requirements
        - Inputs
        - Outputs
        - Constraints
"""
)
