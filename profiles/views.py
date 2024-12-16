from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile

# Create your views here.

def store_file(file):  ## file is a name for paramiter 
        with open("temp/image.jpg","wb+") as dest:   # dest is identifier we assign for location and file will be open and save their i.e temp/...
            for chunk in file.chunks(): #file.chunks is methode to read file in chunks to manage memory 
                dest.write(chunk)

class CreateProfileView(View):
    

    def get(self, request):
        form=ProfileForm()
        return render(request, "profiles/create_profile.html",{
             "form":form
        })

    def post(self, request):

        submitted_form=ProfileForm(request.POST,request.FILES)
        if submitted_form.is_valid():
       # print(request.FILES["image"])# image is name assign to form's input cause there can be multiple file uplodes in same form
        #store_file(request.FILES["image"]) #calling function and passing that file as argement name as file in there
             profile= UserProfile(image=request.FILES["user_image"]) #file is named as user_image in form
             profile.save()
             return HttpResponseRedirect("/profiles")
        return render(request,"profiles/create_profile.html",{
             "form": submitted_form
        })


