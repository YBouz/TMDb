from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Movie, Review


# Create your views here.
def home(request):
    context = {
        'movies': Movie.objects.all()
    }
    return render(request, 'tmdb/home.html', context)


class MovieListView(ListView):
    model = Movie

    # <app>/<model>_<viewtype>.html
    template_name = 'tmdb/home.html'
    context_object_name = 'movies'
    ordering = ['-year']
    paginate_by = 5


class MovieDetailView(DetailView):
    model = Movie


class MovieSearchView(ListView):
    model = Movie
    template_name = 'tmdb/movie_search.html'
    context_object_name = 'movies_search'

    def get_queryset(self):
        result = super(MovieSearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Movie.objects.filter(Q(title__contains=query) | Q(directors__contains=query))
            result = postresult
        else:
            result = None
        return result


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['rating', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user

        movie = self.get_object()
        form.instance.movie = movie
        return super().form_valid(form)


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['rating', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True
        return False


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = '/'

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True
        return False
