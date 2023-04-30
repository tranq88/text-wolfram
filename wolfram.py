import requests
import json


def query_wolfram(app_id: str, query: str, user_num: str) -> str:
    """
    Query the WolframAlpha Conversational API with key <app_id> and
    return the resulting response.
    """
    with open('conversations.json', 'r') as f:
        convos = json.load(f)  # load the json file into a dict

    try:
        # if the number already has an existing conversation
        if user_num in convos:
            conv_id = convos[user_num]['conversationID']
            host = convos[user_num]['host']
            s = convos[user_num]['s']

            url = (
                f'http://{host}/api/v1/conversation.jsp?appid={app_id}&'
                f'conversationid={conv_id}&i={query}'
            )
            if s:
                url += f'&s={s}'

            r = requests.get(url)
            result = r.json()  # store response in a dict

            # update conversations.json for the next query
            convos[user_num]['conversationID'] = result['conversationID']
            convos[user_num]['host'] = result['host']
            if 's' in result:
                convos[user_num]['s'] = result['s']
            else:
                convos[user_num]['s'] = None

            with open('conversations.json', 'w') as f:
                json.dump(convos, f, indent=4)

            return result['result']

        # first-time users
        url = (
            f'http://api.wolframalpha.com/v1/conversation.jsp?'
            f'appid={app_id}&i={query}'
        )
        r = requests.get(url)
        result = r.json()

        if 's' not in result:
            result['s'] = None

        # create new user entry
        # we don't care about storing the result
        ret = result['result']
        result.pop('result')
        convos[user_num] = result

        with open('conversations.json', 'w') as f:
            json.dump(convos, f, indent=4)

        return ret
    except KeyError:
        return "Sorry, I don't understand."
