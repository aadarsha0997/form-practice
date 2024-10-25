from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic import ListView,DetailView,FormView,TemplateView,CreateView



# Create your views here.

####### class base view extemd from basic view #######
# class ReviewView(View):
#     def get(self,request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html",{
#             "form": form
#         })
    

#     def post(self,request):
#         form= ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("thank-you")
#         return render(request,"reviews/review.html",{
#             "form": form
#         })

####### class base view extemd from formview #######
# class ReviewView(FormView):
#     form_class= ReviewForm  ### form name assining
#     template_name="reviews/review.html"
#     success_url ="/thank-you"

#### extending from creat view to save form  #### 
class ReviewView(CreateView):
    model= Review  #### pointing our model
    form_class= ReviewForm  ### pointing our form
    template_name="reviews/review.html"
    success_url="/thank-you"

#### form saving in this formview
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    


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


#### function base view#### of thankyou

# def thank_you (request):


#### Class base view#### of thankyou

# class ThankYouView(View):
#     def get(self,request):
#         return render(request,"reviews/thank-you.html")


####### class base view but specific for returning templete ####
class ThankYouView(TemplateView):

    template_name="reviews/thank-you.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This  really works"
        return context
######### extending from templateview ####
# class ReviewsListView(TemplateView):
#     template_name="reviews/review-list.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review= Review.objects.all()
#         context["reviews"] = review
#         return context

##### same template extending from listview because it is more specific #######

class ReviewsListView(ListView):
    template_name ="reviews/review-list.html"
    model = Review  ### pointing to model from which it have to fetch data
    context_object_name = "reviews"  #### assining name to it to get data in template / by defult it is 0bject_list

    def get_queryset(self):

        base_quary=super().get_queryset()
        data=base_quary.filter(rating__gt=4) #### only show review greater than 4 i.e 5
        return data
    
##### extending from templateview ####
# class DetailView(TemplateView):
#     template_name="reviews/detail-view.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         selected_id=kwargs["id"]
#         selected_review=Review.objects.get(pk=selected_id)
#         context["review"] = selected_review
#         return context


##### extending from detailview ####
class DetailView(DetailView):
    template_name="reviews/detail-view.html"
    model=Review

    
    
    
