from django import forms

class ReviewForm(forms.Form):
    user_name=forms.CharField(label="Your name",max_length=20,error_messages={
        "required":"Your must not be empty",
        "max_length":"Please Enter Shoter Name"
    })
