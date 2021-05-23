from django.urls import path
from .views import (
    TitleListView, TitleDetailView, TitleSearchView, MovieListView, ShowListView, LatestListView, TopRatedListView,
    PersonListView, PersonDetailView
)
from . import views

urlpatterns = [
    path('', TitleListView.as_view(), name='tmdb-home'),
    path('movies/', MovieListView.as_view(), name='tmdb-movies'),
    path('shows/', ShowListView.as_view(), name='tmdb-shows'),
    path('latest/', LatestListView.as_view(), name='tmdb-latest'),
    path('top/', TopRatedListView.as_view(), name='tmdb-top'),
    path('results/', TitleSearchView.as_view(), name='title-search'),
    path('title/<int:pk>/', TitleDetailView.as_view(), name='title-detail'),
    # path('title/<int:pk>/review-create/', ReviewCreateView.as_view(), name='review-create'),
    # path('title/<int:pk>/review-update/', ReviewUpdateView.as_view(), name='review-update'),
    # path('title/<int:pk>/review-delete/', ReviewDeleteView.as_view(), name='review-delete'),
    path('title/<int:titlePK>/review_create/', views.createReview, name='review-create'),
    path('title/<int:titlePK>/review_update/<int:pk>/', views.updateReview, name='review-update'),
    path('title/<int:titlePK>/review_delete/<int:pk>/', views.deleteReview, name='review-delete'),
    path('persons/', PersonListView.as_view(), name='tmdb-persons'),
    path('person/<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
]
