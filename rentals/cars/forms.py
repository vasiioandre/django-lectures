from django import forms
from .models import Review
from django.forms import ModelForm


# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name', max_length=30)
#     last_name = forms.CharField(label='Last Name', max_length=30)
#     email = forms.CharField(label='Last Name', max_length=30)
#     review = forms.CharField(label='Feedback', max_length=200, widget=forms.Textarea(attrs={'class': 'myform'}))

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        # fields = ['first_name', 'last_name', 'stars']
        fields = "__all__"

        labels = {
            "first_name": "YOUR FIRST NAME",
            "last_name": "Last Name",
            "stars": "Review"
        }

        error_messages = {
            "stars": {
                "min_value": "Yo, min value is 1!",
                "max_value": "Yo, max value is 5!"
            }
        }
