from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms


# Create your views here.

def review(request):
    if request.method== 'POST':
        entered_username=request.POST['username']
        if entered_username=="":
         return render(request,"reviews/review.html",{
            "error":True
         })

        print(entered_username)
        return HttpResponseRedirect("/thanks")
    return render(request,"reviews/review.html")
def thank_you (request):
    return render(request,"reviews/thank-you.html")