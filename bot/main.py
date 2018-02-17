from flask import Blueprint, request, current_app as app
from twilio.twiml.messaging_response import Message, MessagingResponse
from twilio.rest import Client
import requests
import cv2
import pyzbar.pyzbar as zbar

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

    # Interpret message.
    response = MessagingResponse()
    if message == 'hello':
        response.message = 'ethdenv woooo!'
    if media_url:
        # Save the image of the qrcode the root dir.
        _save_qrcode(media_url)

        # Read qrcode.
        # Only get 1st code. (ignore multiple qr codes in same image)
        code = _decode_qrcode()
        if not code:
            response.message = 'Hmmm, my vision must be bad. Can you send me your qr code again?'
        else:
            response.message = 'All set up!'
            print(code)

    # Send response to user as sms.
    client.messages.create(to=from_number, from_=account_num, body=response.message)

    return str(response)


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