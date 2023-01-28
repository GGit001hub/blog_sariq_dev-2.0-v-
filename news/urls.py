from django.urls import path
from .views import (
    NewsListView,NewCreateView,
    NewDeleteView,NewDetailView,
    NewUpdateView

)
urlpatterns = [
    path('<int:pk>/edit',NewUpdateView.as_view(),name='new_edit'),
    path('<int:pk>/delete',NewDeleteView.as_view(),name='new_delete'),
    path('<int:pk>/',NewDetailView.as_view(),name='new_detail'),
    path('create/',NewCreateView.as_view(),name='new_create'),
    path('',NewsListView.as_view(),name='news'),
]