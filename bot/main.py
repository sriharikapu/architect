from flask import Blueprint, request, current_app as app
from twilio.twiml.messaging_response import Message, MessagingResponse
from twilio.rest import Client
import requests

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
    from_number = request.form['From']
    message_sid = request.form['MessageSid']
    media_url = request.form['MediaUrl0']
    media_type = request.form['MediaContentType0']
    print(media_url, media_type)

    # Interpret message.
    response = MessagingResponse()
    if message == 'hello':
        response.message = 'ethdenv woooo!'
    if media_url:
        with open('output.jpg', 'wb') as image:
            image.write(requests.get(media_url).content)
        response.message = 'thank you for joining!'
        


    # Send response to user as sms.
    client.messages.create(to=from_number, from_=account_num, body=response.message)

    return str(response)

