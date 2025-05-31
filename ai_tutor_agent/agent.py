from google.adk.agents import Agent
from . import prompt
from .sub_agents.math_agent.agent import math_agent
from .sub_agents.physics_agent.agent import physics_agent

root_agent = Agent(
    name="ai_tutor_agent",
    model = "gemini-2.5-flash-preview-05-20",
    description="A tutor agent that helps with various queries.",
    instruction=prompt.ai_tutor_instructions,
    sub_agents = [math_agent, physics_agent],
)