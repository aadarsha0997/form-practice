from django import forms 
from .models import Review

# class ReviewForm(forms.Form):
#     user_name=forms.CharField(label="Your name",max_length=20,error_messages={
#         "required":"Your must not be empty",
#         "max_length":"Please Enter Shoter Name"
#     })
#     review_text =forms.CharField(label="Your feedback",widget=forms.Textarea,max_length=200)
#     rating=forms.IntegerField(label="Your Rating",min_value=1,max_value=5)


##### take model as a form ######
class ReviewForm(forms.ModelForm):
    class Meta:
        model= Review
        fields ='__all__'
        labels={
            "user_name": "Your Name",
            "review_text":"Your Feedback",
            "rating":"Your rating"
        }
        error_messages={
            "user_name": {
                "required":"your name must not be empty",
                "max_length":"Its too long"
            }
        }
        # exclude= " djjd jsj field name" if you want to excludeRe