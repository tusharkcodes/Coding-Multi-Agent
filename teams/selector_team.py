from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from models import model

from agents.requirement_agent import requirement_agent
from agents.coding_agent import coding_agent
from agents.review_agent import review_agent
from agents.docs_agent import docs_agent
from agents.test_agent import test_agent
from agents.deploy_agent import deploy_agent

selector_team = SelectorGroupChat(
    participants =[
        requirement_agent,
        coding_agent,
        review_agent,
        docs_agent,
        test_agent,
        deploy_agent
    ],
    model_client=model,
    termination_condition=TextMentionTermination("END"),
    selector_prompt="""
Workflow rules:
1. Start with RequirementAgent
2. Then CodingAgent
3. Then ReviewAgent
4. If ReviewAgent says APPROVED → continue
5. Else → return to CodingAgent
6. Finish with DeployAgent
"""
)
