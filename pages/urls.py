from django.urls import path
from .views import BoshViews

urlpatterns = [
    path('',BoshViews.as_view(),name='home')
]