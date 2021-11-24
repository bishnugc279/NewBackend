from django import forms
from .models import Inbox

class InboxForm(forms.ModelForm):
    class Meta:
        model = Inbox
        fields = (
            'inbox_id',
            'inbox_title',
            'inbox_description',
            'inbox_date',
            'user_id',
            'status',
            'update_date',
            'clientuser_address',
            'operater_reply',
            'client_id'
            )