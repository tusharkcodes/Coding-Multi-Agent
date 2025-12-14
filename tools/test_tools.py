import subprocess
from autogen_core.tools import FunctionTool

def run_tests() -> str:
    result = subprocess.run(
        ["pytest"],
        capture_output=True,
        text=True
    )
    return result.stdout + result.stderr

run_tests_tool = FunctionTool(
    name="run_tests",
    description="Run pytest and return test results",
    func=run_tests
)
