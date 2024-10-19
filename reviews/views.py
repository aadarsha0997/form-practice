from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View



# Create your views here.

####### class base view #######
class ReviewView(View):
    def get(self,request):
        form = ReviewForm()
        return render(request, "reviews/review.html",{
            "form": form
        })
    

    def post(self,request):
        form= ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("thank-you")
        return render(request,"reviews/review.html",{
            "form": form
        })
        ##### function base view ######
# def review(request):
#     if request.method== 'POST':
#         form=ReviewForm(request.POST)

#         if form.is_valid():
#             ######### Normal way to save user_given data to database ########
#             #review=Review(user_name=form.cleaned_data['user_name'],review_text=form.cleaned_data['review_text'],rating=form.cleaned_data['rating'])
#             # review.save()
#             ##########

#             ###### Saving user given data in formModel #########
#             form.save()
#             ####
#             return HttpResponseRedirect("/thanks")
#     else:
#         form=ReviewForm()
        
#     return render(request,"reviews/review.html",{
#         "form":form
#     })
def thank_you (request):
    return render(request,"reviews/thank-you.html")