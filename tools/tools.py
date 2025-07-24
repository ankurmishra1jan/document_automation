from langchain_core.tools import tool
from langchain_tavily import TavilySearch
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
        search_tool = TavilySearch(
            max_results=5,
            topic="general"
        )
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
def format_invoice(invoice_type: str, invoice_number: str, invoice_date: str, due_date: str, items: list):
    """
    Based on user data or query, this will provide billing related invoice with signoff placeholder in tabular with border format based on user data and query
    :param :
    :return:
    """
    prompt_query = f"""
        you are specialized agent to create invoice format with signoff placeholder in tabular with border based on given information below:
        invoice_type : {invoice_type}
        invoice_number: {invoice_number}
        invoice_date: {invoice_date}
        due_date: {due_date}
        items: {items}
    """

    llm_model_obj = GetLLMReturn()
    getllm = llm_model_obj.get_model()
    response = getllm.invoke(prompt_query)
    return {"messages": response}


@tool(args_schema=FormatCreationArgs)
def format_offerletter(invoice_type: str, invoice_number: str, invoice_date: str, due_date: str, items: list):
    """
    Based on user data or query, this will provide billing related employment offer letter with signoff placeholder in tabular with border format based on user data and query
    :param :
    :return:
    """
    prompt_query = f"""
        Based on user data or query, this will provide billing related invoice, recipient and employment offer letter with signoff placeholder in tabular with border format based on user data and query.
        invoice_type : {invoice_type}
        invoice_number: {invoice_number}
        invoice_date: {invoice_date}
        due_date: {due_date}
        items: {items}
    """

    llm_model_obj = GetLLMReturn()
    getllm = llm_model_obj.get_model()
    response = getllm.invoke(prompt_query)
    return {"messages": response}


@tool(args_schema=FormatCreationArgs)
def format_recipient(invoice_type: str, invoice_number: str, invoice_date: str, due_date: str, items: list):
    """
    Based on user data or query, this will provide billing related recipient with signoff placeholder in tabular with border format based on user data and query
    :param :
    :return:
    """
    prompt_query = f"""
        Based on user data or query, this will provide billing related invoice, recipient and employment offer letter with signoff placeholder in tabular with border format based on user data and query.
        invoice_type : {invoice_type}
        invoice_number: {invoice_number}
        invoice_date: {invoice_date}
        due_date: {due_date}
        items: {items}
    """

    llm_model_obj = GetLLMReturn()
    getllm = llm_model_obj.get_model()
    response = getllm.invoke(prompt_query)
    return {"messages": response}

