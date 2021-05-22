from django.urls import path
from .views import TitleListView, TitleDetailView, TitleSearchView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView
from . import views

urlpatterns = [
    path('', TitleListView.as_view(), name='tmdb-home'),
    path('movie/<int:pk>/', TitleDetailView.as_view(), name='title-detail'),
    path('movie/<int:pk>/new/', ReviewCreateView.as_view(), name='review-create'),
    path('movie/<int:pk>/update/', ReviewUpdateView.as_view(), name='review-update'),
    path('movie/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
    path('results/', TitleSearchView.as_view(), name='title-search'),
]