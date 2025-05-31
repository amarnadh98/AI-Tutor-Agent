from google.adk.agents import Agent
from . import prompt
# from ...config import MODEL
MODEL = "gemini-2.5-flash-preview-05-20"

math_agent = Agent(
    name="math_agent",
    model = MODEL,
    instruction=prompt.math_agent_instructions
)
