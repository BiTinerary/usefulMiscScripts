from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from scripts import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    body = body.lower()
    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == 'hello':
        resp.message("Hi!")

    elif body == 'bye':
        resp.message("Goodbye")

    elif body == 'snow':
        resp.message(snowEmer.status())

    elif body == 'rat':
        resp.message(smallRat.getIP())

    elif 'coin' in body:
        resp.message('%s\n%s' % (getCoin.coinMarket(body), getCoin.coinGecko(body)))

    else:
        resp.message("Hellow Monkey")
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)

