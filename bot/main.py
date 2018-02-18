from flask import Blueprint, request, make_response, current_app as app
from twilio.twiml.messaging_response import Message, MessagingResponse
from twilio.rest import Client
import requests
import cv2
import pyzbar.pyzbar as zbar
from bot.ethdenver_bot import get_response

main = Blueprint('main', __name__)

@main.route('/', methods=['POST'])
def index():
    # Twilio client.
    account_sid = app.config['TWILIO_ACCOUNT_SID']
    auth_token = app.config['TWILIO_AUTH_TOKEN']
    account_num = app.config['TWILIO_NUMBER']
    client = Client(account_sid, auth_token)

    # Get message info from sms.
    user_message = request.form['Body'].lower()
    from_number = request.form['From']
    message_sid = request.form['MessageSid']
    media_url = request.form.get('MediaUrl0', None)
    media_type = request.form.get('MediaContentType0', None)

    # Get cookies 🍪🍪🍪
    prev_response = request.cookies.get('prev_response', None)
    name = request.cookies.get('name', None)
    code = request.cookies.get('qrcode', None)

    # Handle account creation.
    user_sent_qrcode = media_url and media_type
    # Save and decode qrcode sent by new user.
    if user_sent_qrcode:
        _save_qrcode(media_url)
        code = _decode_qrcode()
        if code:
            code = code[0].data
            user_message = 'yes:qrcode'
        else:
            user_message = 'no:qrcode'

    # Interpret message.
    print('prev_response: {}'.format(prev_response))
    if prev_response:
        mudged = user_message
        # User responded to name request.
        if 'your name?' in prev_response:
            # Reduce the message down to just the user's name.
            mudged = ''.join([word for word in mudged.split(' ') if word not in ['my', 'name', 'is', 'i\'m', 'i am']])
            name = mudged
            mudged = mudged + ':name'
        # User responded to account creation.
        if 'Archethtect account?' in prev_response:
            mudged = mudged + ':account'
        # User responded to option to see proposals on queue or learn more about arch.
        if 'proposals or arch' in prev_response and any(choice in mudged for choice in ['proposals', 'arch']):
            mudged = 'yes:' + mudged
        # Update user_message to bot readable format.
        user_message = mudged

    # Create resonse.
    response = MessagingResponse()
    print('user_message: {}'.format(user_message))
    response.message = get_response(user_message)
    flask_resp = make_response(str(response))

    # Update cookies.
    flask_resp.set_cookie('prev_response', response.message)
    if name:
        flask_resp.set_cookie('user_name', name)
    if code:
        flask_resp.set_cookie('qrcode', code)
    # Send response to user as sms.
    client.messages.create(to=from_number, from_=account_num, body=response.message)

    return flask_resp


def _save_qrcode(media_url):
    # Download image from twilio media url.
    with open('qr-code.jpg', 'wb') as image:
            image.write(requests.get(media_url).content)

    # Open image as grayscale.
    gray_image = cv2.imread('qr-code.jpg', cv2.IMREAD_GRAYSCALE)
    # Convert to black and white.
    _, bw_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # Swap black and white to make qrcode appear 
    cv2.imwrite('qr-code.jpg', (255 - bw_image))


def _decode_qrcode():
    img = cv2.imread('qr-code.jpg')
    return zbar.decode(img)