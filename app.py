from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/VSM-COVID Helpline Activity', methods=['POST'])
def Reply_To_Query_Message():
    incoming_message = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if 'total' or 'beneficiaries' in incoming_message:
        total_beneficiaries_count = 3077
        msg.body(total_beneficiaries_count)
        responded = True

    if 'male' or 'beneficiaries' in incoming_message:
        total_beneficiaries_count = 3077
        msg.body(total_beneficiaries_count)
        responded = True

    if 'female' or 'beneficiaries' in incoming_message:
        total_beneficiaries_count = 3077
        msg.body(total_beneficiaries_count)
        responded = True

    if 'children' or 'beneficiaries' in incoming_message:
        total_beneficiaries_count = 3077
        msg.body(total_beneficiaries_count)
        responded = True

    if 'goa' or 'beneficiaries' in incoming_message:
        total_beneficiaries_count = 3077
        msg.body(total_beneficiaries_count)
        responded = True

    if 'nashik' or 'beneficiaries' in incoming_message:
        total_beneficiaries_count = 3077
        msg.body(total_beneficiaries_count)
        responded = True

    if 'pune' or 'beneficiaries' in incoming_message:
        total_beneficiaries_count = 3077
        msg.body(total_beneficiaries_count)
        responded = True

    if 'thane' or 'beneficiaries' in incoming_message:
        total_beneficiaries_count = 3077
        msg.body(total_beneficiaries_count)
        responded = True

    if 'goa' or 'beneficiaries' in incoming_message:
        total_beneficiaries_count = 3077
        msg.body(total_beneficiaries_count)
        responded = True

    if not responded:
        msg.body("We have only these many parameters as of now with us")

    return str(resp)


if __name__ == '__main__':
    app.run()
