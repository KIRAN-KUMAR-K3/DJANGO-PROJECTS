from django import forms
class StringConverterForm(forms.Form):
    input_string = forms.CharField(label='Input String', widget=forms.TextInput)
    CASE_CHOICES = [
    ('upper', 'ALL CAPITAL CASE'),
    ('title', 'Title Case'),
    ('lower', 'all lower case'),
    ('sentence', 'Sentence case'),
    ]
    case_choice = forms.ChoiceField(choices=CASE_CHOICES, widget=forms.RadioSelect)