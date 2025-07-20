from langchain_core.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
from model.models import InvoiceItem, FormatCreationArgs
import traceback
from largemodel.groq_model import GetLLMReturn
from langchain.globals import set_verbose
set_verbose(True)



@tool
def latest_news_based_on_query(arg)-> str:
    """
    Based on user query, this will search the data in TavilySearchResults for get the latest news related
    :param query:
    :return:
    """
    try:
        search_tool = TavilySearchResults()
        response = search_tool.invoke(arg)
        return {"messages": response}
    except Exception:
        traceback.print_exc()

@tool
def format_create(query: InvoiceItem):
    """
    Based on user data or query, this will provide billing related invoice, recipient and employment offer letter with signoff placeholder in tabular with border format based on user data and query
    :param query:
    :return:
    """
    prompt_query = f"""
        Based on user data or query, this will provide billing related invoice, recipient and employment offer letter with signoff placeholder in tabular with border format based on user data and query {query}
    """
    llm_model_obj = GetLLMReturn()
    getllm = llm_model_obj.get_model()
    response = getllm.invoke(prompt_query)
    return {"messages": response}

@tool(args_schema=FormatCreationArgs)
def format_creation(invoice_type: str, recipient_name: str, recipient_address: str,
                    invoice_number: str, invoice_date: str, due_date: str, items: list) -> str:
    """
    Based on user data or query, this will provide billing related invoice, recipient and employment offer letter with signoff placeholder in tabular with border format based on user data and query
    :param :
    :return:
    """
    prompt_query = f"""
        Based on user data or query, this will provide billing related invoice, recipient and employment offer letter with signoff placeholder in tabular with border format based on user data and query.
        invoice_type : {invoice_type}
        recipient_name: {recipient_name}
        recipient_address: {recipient_address}
        invoice_number: {invoice_number}
        invoice_date: {invoice_date}
        due_date: {due_date}
        items: {items}
    """
    llm_model_obj = GetLLMReturn()
    getllm = llm_model_obj.get_model()
    response = getllm.invoke(prompt_query)
    return {"messages": response}


