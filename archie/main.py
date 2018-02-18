from flask import Blueprint, request, make_response, current_app as app
from twilio.twiml.messaging_response import Message, MessagingResponse
from twilio.rest import Client
import requests
import cv2
import pyzbar.pyzbar as zbar
from archie.bot import get_response

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
    name = request.cookies.get('user_name', None)
    code = request.cookies.get('qrcode', None)
    
    user_done_with_demo = 'https://github.com/Meeshbhoombah/architect' in prev_response

    # if user_done_with_demo:
    # Handle account creation.
    user_sent_qrcode = media_url and media_type
    # Save and decode qrcode sent by new user.
    if user_sent_qrcode:
        _save_qrcode(media_url)
        code = _decode_qrcode()
        print(code)
        if code:
            code = code[0].data
            user_message = 'yes:qrcode'
        else:
            user_message = 'no:qrcode'

    # Interpret message.
    user_intent = user_message  
    if prev_response:
        user_intent = _guess_user_intent(user_message, prev_response)

    # Create resonse.
    response = MessagingResponse()
    response.message = get_response(user_intent)
    flask_resp = make_response(str(response))

    # Update cookies.
    if response.message:
        flask_resp.set_cookie('prev_response', response.message)
    else:
        response.message = prev_response

    if name:
        flask_resp.set_cookie('user_name', name)
    if code:
        flask_resp.set_cookie('qrcode', code)

    # if name and code:
    #     user = {
    #         'id': code.rsplit('/', 1)[-1],
    #         'first_name': name
    #     }
    #     resp = requests.post('http://beb7d5ba.ngrok.io/user/', json=user)
    #     print(resp)
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


def _guess_user_intent(user_message, bot_prev_response):
    intent = user_message
    # User responded to name request.
    if 'your name?' in bot_prev_response:
        # Reduce the message down to just the user's name.
        intent = ''.join([word for word in intent.split(' ') if word not in ['my', 'name', 'is', 'i\'m', 'i am']])
        intent = intent
        intent = intent + ':name'
    # User responded to account creation.
    if 'Archethtect account?' in bot_prev_response:
        intent = intent + ':account'
    # User responded to option to see proposals on queue or learn more about arch.
    if 'proposals or arch' in bot_prev_response and any(choice in intent for choice in ['proposals', 'arch']):
        intent = 'yes:' + intent
    # User reponded to picking a proposal.
    if 'queue for voting.' in bot_prev_response:
        if 'wifi' in user_message:
            intent = 'yes:wifi'
        if 'ceremonies' in user_message:
            intent = 'yes:ceremonies'
        if 'food' in user_message:
            intent = 'yes:food'
        if 'more' in user_message:
            intent = 'yes:more'
        # User responded to seeing categories.
        if 'category' in user_message:
            intent = 'yes:category'
    # User responded to picking category.
    if 'which category' in bot_prev_response:
        intent = 'soon'
    
    return intent
        