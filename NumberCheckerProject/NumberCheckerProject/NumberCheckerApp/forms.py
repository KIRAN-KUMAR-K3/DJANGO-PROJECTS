from django import forms
class NumberCheckForm(forms.Form):
    number = forms.IntegerField(label='Enter a number')
    is_prime = forms.BooleanField(label='Check if prime', required=False)
    is_even = forms.BooleanField(label='Check if even', required=False)
    is_odd = forms.BooleanField(label='Check if odd', required=False)
    is_perfect_square = forms.BooleanField(label='Check if perfect square', required=False)