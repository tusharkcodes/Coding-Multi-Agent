from autogen_agentchat.agents import AssistantAgent
from models import model

deploy_agent = AssistantAgent(
    name="DeployAgent",
    model_client=model,
    system_message="""
Generate deployment steps including:
- venv setup
- dependency installation
- run instructions
"""
)
