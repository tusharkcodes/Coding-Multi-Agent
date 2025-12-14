from autogen_agentchat.agents import AssistantAgent
from models import model

docs_agent = AssistantAgent(
    name="DocsAgent",
    model_client=model,
    system_message="""
Generate structured documentation including:
- Overview
- Function explanations
- Usage examples
"""
)
