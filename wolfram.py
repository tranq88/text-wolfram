import requests


def query_wolfram(app_id: str, query: str) -> str:
    """
    Query the WolframAlpha Short Answers API with key <app_id> and
    return the result.
    """
    url = f'http://api.wolframalpha.com/v1/result?appid={app_id}&i={query}'

    r = requests.get(url)
    return r.text
