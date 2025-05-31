from google.adk.agents import Agent
from . import prompt
# from ...config import MODEL
MODEL = "gemini-2.5-flash-preview-05-20" 

physics_agent = Agent(
    name="physics_agent",
    model = MODEL,
    instruction=prompt.physics_agent_instructions,
    # tools=[
        
    # ]
)