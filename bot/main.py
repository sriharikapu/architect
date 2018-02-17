from flask import Blueprint, request, current_app as app
from twilio.twiml.messaging_response import Message, MessagingResponse
from twilio.rest import Client

main = Blueprint('main', __name__)

@main.route('/', methods=['POST'])
def index():
    # Twilio client.
    account_sid = app.config['TWILIO_ACCOUNT_SID']
    auth_token = app.config['TWILIO_AUTH_TOKEN']
    account_num = app.config['TWILIO_NUMBER']
    client = Client(account_sid, auth_token)

    # Get message info from sms.
    message = request.form['Body']
    msg_from = request.form['From']

    # Interpret message.
    response = MessagingResponse()
    if message == 'hello':
        response.message = 'ethdenv woooo!'

    # Send response to user as sms.
    client.messages.create(to=msg_from, from_=account_num, body=response.message)

    return str(response)