# orchestrator.py
from teams.round_robin_team import round_robin_team
from teams.selector_team import selector_team

async def stream_round_robin(task: str):
    async for event in round_robin_team.run_stream(task=task):
        yield event

async def stream_selector(task: str):
    async for event in selector_team.run_stream(task=task):
        yield event
