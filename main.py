import requests
from twilio.rest import Client
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
# Set environment variables for your credentials
account_sid = "INSERT TWILIO ACCOUNT SID HERE"
auth_token = "INSERT TOKEN HERE"
client = Client(account_sid, auth_token)

# client.messages.create(body, from, to), body is the message, from is the twilio number, to is where we send to

app = Flask(__name__)


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Get the incoming message
    incoming_msg = request.values.get('Body', '')

    # Create a Twilio response object
    resp = MessagingResponse()



# incoming_msg is what is received, pass into wolfram and pass the response into the thing below
    resp.message(wolfram(input(incoming_msg)))
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)