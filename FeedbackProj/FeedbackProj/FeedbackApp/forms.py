# forms.py in FeedbackApp
from django import forms
from .models import Contact

TOPIC_CHOICES = [
    ('general', 'General'),
    ('feedback', 'Feedback'),
    ('inquiry', 'Inquiry'),
]

class ContactForm(forms.ModelForm):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES)

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'topic']
