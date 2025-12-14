from autogen_agentchat.agents import AssistantAgent
from models import model
import asyncio

coding_agent = AssistantAgent(
    name="CodingAgent",
    model_client=model,
    
    system_message="""
Generate clean, well-structured Python code.

IMPORTANT:
- Do NOT save files
- Return ONLY the code in a single code block 
- If code is proper then return APPROVED
"""
)
