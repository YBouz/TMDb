from django.urls import path
from .views import (
    TitleListView, TitleDetailView, TitleSearchView, MovieListView, ShowListView, LatestListView, TopRatedListView,
    PersonListView, PersonDetailView,
    ChartsListView
)
from . import views

urlpatterns = [
    path('', ChartsListView.as_view(), name='tmdb-home'),
    path('browse/', TitleListView.as_view(), name='tmdb-browse'),
    path('movies/', MovieListView.as_view(), name='tmdb-movies'),
    path('shows/', ShowListView.as_view(), name='tmdb-shows'),
    path('latest/', LatestListView.as_view(), name='tmdb-latest'),
    path('top/', TopRatedListView.as_view(), name='tmdb-top'),
    path('genres/', views.genreView, name='tmdb-genre'),
    path('results/', TitleSearchView.as_view(), name='title-search'),
    path('title/<int:pk>/', TitleDetailView.as_view(), name='title-detail'),
    path('title/<int:titlePK>/review_create/', views.createReview, name='review-create'),
    path('title/<int:titlePK>/review_update/<int:pk>/', views.updateReview, name='review-update'),
    path('title/<int:titlePK>/review_delete/<int:pk>/', views.deleteReview, name='review-delete'),
    path('persons/', PersonListView.as_view(), name='tmdb-persons'),
    path('person/<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
]
