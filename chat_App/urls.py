from django.urls import path
from .views import home, get_bot_response,ChatBotView



urlpatterns = [
    #path('', home, name='home'),
    #path('get_bot_response/', get_bot_response, name='get_bot_response'),
    path('chatbot/', ChatBotView.as_view(), name='chatbot'),
]
