from django import forms
class CalculatorForm(forms.Form):
    number1 = forms.IntegerField(label='First Number')
    number2 = forms.IntegerField(label='Second Number')
    OPERATION_CHOICES = [
        ('add', 'Addition'),
        ('subtract', 'Subtraction'),
        ('multiply', 'Multiplication'),
        ('divide', 'Division'),
        ('moddiv','ModDivision')
    ]
    operation = forms.ChoiceField(choices=OPERATION_CHOICES)