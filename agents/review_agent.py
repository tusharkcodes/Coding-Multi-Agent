from autogen_agentchat.agents import AssistantAgent
from models import model
import asyncio

review_agent = AssistantAgent(
    name="ReviewAgent",
    model_client=model,
    system_message="""
Review the Python code for:
- Correctness
- Efficiency

If acceptable, respond ONLY with:
APPROVED
Otherwise, provide feedback.
"""
)
