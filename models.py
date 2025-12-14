from autogen_ext.models.ollama import OllamaChatCompletionClient

model = OllamaChatCompletionClient(
    model="mistral",
    host="http://localhost:11434",
    temperature=0.2
)
