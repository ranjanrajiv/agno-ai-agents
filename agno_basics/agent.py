from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv

load_dotenv()

# create a database
db = SqliteDb(db_file="chat_history.db")
llm = OpenAIChat(id="gpt-4.1-mini")

agent = Agent(
    name="my_agent",
    model=llm,
    db=db,
    session_id="session_2",
    user_id="user1",
    add_history_to_context=True,
    num_history_runs=5,
    add_session_state_to_context=True,
    markdown=True,
    stream=True
)

response = agent.print_response("Write a short poem about the sea.")