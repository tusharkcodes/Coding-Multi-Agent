from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.ui import Console


from agents.requirement_agent import requirement_agent
from agents.coding_agent import coding_agent
from agents.review_agent import review_agent
from agents.docs_agent import docs_agent
from agents.test_agent import test_agent
from agents.deploy_agent import deploy_agent

round_robin_team = RoundRobinGroupChat(
    participants =[
        requirement_agent,
        coding_agent,
        review_agent,
        docs_agent,
        test_agent,
        deploy_agent
    ],
    termination_condition=TextMentionTermination("END")
)

