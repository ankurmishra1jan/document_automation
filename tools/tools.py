from langchain_core.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
import traceback
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

