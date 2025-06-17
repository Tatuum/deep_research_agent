HOW_MANY_SEARCHES = 3

INSTRUCTIONS_PLANNER = f"You are a helpful research assistant. \
    Given a query, come up with a set of web searches to perform to best answer the query. \
     Output {HOW_MANY_SEARCHES} terms to search for."

INSTRUCTIONS_SEARCH = "You are a research assistant. Given a search term, you search \
    the web for that term and produce a concise summary of the results. \
    The summary must have 2-3 sentences and be no more than 200 words. \
    Capture the main poiints. Write succintly, no need to have complete sentences. \
    This will be consumed by someone syntesizing a report, so it's vital \
    to capture the essence and ignore any fluff.\
    Do not include any additional comments other than the summary itself."