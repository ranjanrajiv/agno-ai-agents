from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

llm = OpenAIChat(id="gpt-4.1-mini")

agent = Agent(name="my_agent",
              model=llm,
              markdown=True,
              stream=True
)

response = agent.print_response("Write a short poem about the sea.")