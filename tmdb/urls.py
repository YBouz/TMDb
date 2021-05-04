from django.urls import path
from .views import MovieListView, MovieDetailView, MovieSearchView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView
from . import views

urlpatterns = [
    path('', MovieListView.as_view(), name='tmdb-home'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movie/<int:pk>/new/', ReviewCreateView.as_view(), name='review-create'),
    path('movie/<int:pk>/update/', ReviewUpdateView.as_view(), name='review-update'),
    path('movie/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
    path('results/', MovieSearchView.as_view(), name='movie-search'),
]