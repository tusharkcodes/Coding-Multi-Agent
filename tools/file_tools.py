from autogen_core.tools import FunctionTool

def save_file(filename: str, content: str) -> str:
    with open(filename, "w") as f:
        f.write(content)
    return f"File '{filename}' saved successfully."

save_file_tool = FunctionTool(
    name="save_file",
    description="Save generated code or text to a file",
    func=save_file
)
