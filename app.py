from fastapi import FastAPI
from pydantic import BaseModel
from agent import DocumentStructureAutomation
from langchain_core.messages import HumanMessage
import os

os.environ.pop("SSL_CERT_FILE", None)

app = FastAPI()

# Define Pydantic model to accept request body
class UserQuery(BaseModel):
    messages: str


agent = DocumentStructureAutomation()

@app.post("/execute")
def execute_agent(user_input: UserQuery):
    app_graph = agent.workflow()

    # Prepare agent state as expected by the workflow
    input_data = [
        HumanMessage(content=user_input.messages)
    ]
    query_data = {
        "messages": input_data,
        "next": "",
        "query": "",
        "current_reasoning": "",
    }
    config_var = {"recursion_limit": 25}
    response = app_graph.invoke(query_data, config=config_var)
    return {"messages": response["messages"]}