from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from wolfram import query_wolfram
from dotenv import load_dotenv
import os


app = Flask(__name__)


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming messages with a WolframAlpha API query response."""
    incoming_msg = request.values.get('Body', '')
    from_number = request.values.get('From', '')
    resp = MessagingResponse()

    load_dotenv()
    app_id = os.getenv('WOLFRAM_APP_ID')

    resp.message(query_wolfram(app_id, incoming_msg, from_number))

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
