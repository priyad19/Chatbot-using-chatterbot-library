from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('ChatBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

def home(request):
    return render(request, 'core/base.html')

def get_bot_response(request):
    user_text = request.GET.get('msg')
    bot_response = str(chatbot.get_response(user_text))
    return JsonResponse({'response': bot_response})

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class ChatBotView(APIView):

    def __init__(self):
        self.chatbot = ChatBot('ChatBot')
        self.trainer = ChatterBotCorpusTrainer(self.chatbot)
        self.trainer.train("chatterbot.corpus.english")

    def post(self, request):
        user_input = request.data.get('message')
        url = "http://your-api-endpoint.com"
        timeout = 5 # set timeout to 5 seconds

        try:
            response = requests.post(url, json={"message": user_input}, timeout=timeout)
            if response.status_code == 200:
                data = {'message': str(self.chatbot.get_response(user_input))}
                return Response({'status': 201, 'success': True, 'data': data, "message": "Success"})
            else:
                return Response({'status': 400, 'success': False, 'message': 'Invalid request'})
        except requests.exceptions.Timeout:
            return Response({'status': 400, 'success': False, 'message': 'The chatbot took too long to respond. Please try again.'})
        except:
            return Response({'status': 400, 'success': False, 'message': 'An error occurred while processing your request. Please try again.'})

