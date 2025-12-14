from autogen_agentchat.agents import AssistantAgent
from models import model
from tools.test_tools import run_tests_tool

test_agent = AssistantAgent(
    name="TestAgent",
    model_client=model,
    tools=[run_tests_tool],
    system_message="""
Generate pytest test cases and execute them using run_tests tool.
"""
)
