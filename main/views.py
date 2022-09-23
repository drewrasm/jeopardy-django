# Create your views here.
from jeopardy.settings import SLACK_OAUTH_TOKEN
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from slack_sdk.web import WebClient

from main.messages import HelloMessage

SLACK_OAUTH_TOKEN = getattr(settings, 'SLACK_OAUTH_TOKEN', None)

client = WebClient(token=SLACK_OAUTH_TOKEN)

class Events(APIView):
    def post(self, request, *args, **kwargs):

        slack_message = request.data

        if slack_message.get('token') != SLACK_OAUTH_TOKEN:
            return Response(status=status.HTTP_403_FORBIDDEN)

        # verification challenge
        if slack_message.get('type') == 'url_verification':
            return Response(data=slack_message, status=status.HTTP_200_OK)   

        return Response(status=status.HTTP_200_OK)

class Hello(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        hello_message = HelloMessage(data['channel_id'])
        message = hello_message.get_message_payload()
        res = Response(status=200)
        res.data = message
        return res