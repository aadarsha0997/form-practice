from django.urls import path
from . import views
urlpatterns = [
    # path("",views.review),   normal function base view
    path("",views.ReviewView.as_view()),
    # path("thank-you",views.thank_you,name="thank-you")   function base view of thankyou post
    path("thank-you",views.ThankYouView.as_view()),
    path("review-list",views.ReviewsListView.as_view()),
    path("review-list/<int:id>",views.DetailView.as_view()),
]
