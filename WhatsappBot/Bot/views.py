from django.shortcuts import render, HttpResponse
# Download the helper library from https://www.twilio.com/docs/python/install
import os,openai
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client
from dotenv import load_dotenv

from WhatsappBot.settings import TWILIO_ACCOUNT_SID,auth_token
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# auth_token = os.getenv("auth_token",None)
# account_sid = os.getenv("account_sid",None)
client = Client(TWILIO_ACCOUNT_SID, auth_token)

load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)


# Create your views here.
@csrf_exempt
def bot(request):
    print(request.POST)
    message = request.POST['Body']
    sender_name = request.POST['ProfileName']
    sender_number = request.POST['From']
    openai.api_key = api_key
    print(message)       
    if message=='hi':
        message = client.messages.create(
                              body=f"Hello there!, {sender_name}",
                              from_='whatsapp:+14155238886',
                              to=sender_number
                       )
    else: 
          prompt = message
          response = openai.Completion.create(
          engine='text-davinci-003',
          prompt=prompt,
          max_tokens=956,
            # stop =
          temperature=0.6
    )
          chatbot_response = response.choices[0].text
          print(chatbot_response)
     
          message = client.messages.create(
                              body=f"Hello {sender_name}, {chatbot_response}",
                              from_='whatsapp:+14155238886',
                              to=sender_number
                       )
    return HttpResponse("5")