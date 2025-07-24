members_dict = {
    "information_node": "specialized agent to provide latest news from the browser based on user query or data",
    "format_creation": "specialized agent to provide invoice, recipient and employment offer letter with signoff placeholder in tabular with border format based on user data and query."
}

options = list(members_dict.keys()) + ["FINISH"]

worker_info = '\n\n'.join([f'WORKER: {member} \nDESCRIPTION: {description}' for member, description in members_dict.items()]) + '\n\nWORKER: FINISH \nDESCRIPTION: If User Query is answered and route to Finished'

system_prompt = (
    "You are a supervisor Agent with managing a conversation between the following workers. if you think, you need any tools then you can pick otherwise handle at your end."
    "### SPECIALIZED ASSISTANT:\n"
    f"{worker_info}\n\n"
    "Your primary role is to analyzie the user query, if you can solve the user query at your end then solve and give the answer. if user query require to any tools help then you can pick and give correct answer of user query with the tools which you have"
    "If a user query to know the search form the browser, you can use your search tool to help them, "
    "If a user query to ask about the invoice, recipient and employment offer letter with signoff placeholder in tabular with border format based on the user data or query, you have multiple tools and you can pick from them based on your reasoning and those tools will help you to create general format."
    "Whatever result you got from information tool, just summarize the result in 100 words. "
    "delegate the task to the appropriate specialized workers. Each worker will perform a task and respond with their results and status. "
    "When all tasks are completed and the user query is resolved, respond with FINISH.\n\n"

    "**IMPORTANT RULES:**\n"
    "1. If the user's query is clearly answered and no further action is needed, respond with FINISH.\n"
    "2. If you detect repeated or circular conversations, or no useful progress after multiple turns, return FINISH.\n"
    "3. If more than 10 total steps have occurred in this session, immediately respond with FINISH to prevent infinite recursion.\n"
    "4. Always use previous context and results to determine if the user's intent has been satisfied. If it has — FINISH.\n"
)