from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

class GetLLMReturn:

    def __init__(self, model="gemma2-9b-it", temp=0.2):
        self.temperature = temp
        self.model = model
        self.groq_model = ChatGroq(model_name=self.model, temperature=self.temperature, max_tokens=4000)

    def get_model(self):
        return self.groq_model


if __name__ == "__main__":
    llm_model_instance = GetLLMReturn()
    model = llm_model_instance.get_model()
    response = model.invoke("please create one invoice of 4 product which have 2 mangos, 3 apples, 1 orange, 2 bananas with 20,40,35 and 50 corresponding prices with tabular format as well as signoff placeholder.")
    print(response)