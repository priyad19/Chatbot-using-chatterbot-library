from django.contrib import admin
from .models import Conversation

@admin.register(Conversation)
class DataAdmin(admin.ModelAdmin):
    list_display = ('input_text', 'response_text', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('input_text', 'response_text')
