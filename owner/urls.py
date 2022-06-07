from owner.views import * 
from django.urls import path


urlpatterns = [
    path('',OwnerView.as_view()),
    path('/owner',OwnerView.as_view()),
    path('/dog',DogView.as_view())
]
