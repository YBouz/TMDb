from django.shortcuts import render
from django.db.models import Avg
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Title, TitleReview, Person


# Create your views here.
class PersonListView(ListView):
    model = Person
    template_name = 'tmdb/person_list.html'
    context_object_name = 'persons'
    ordering = ['name']
    paginate_by = 5


class PersonDetailView(DetailView):
    model = Person


class TitleListView(ListView):
    model = Title
    template_name = 'tmdb/home.html'
    context_object_name = 'titles'
    queryset = Title.objects.annotate(
        avg_rating=Avg('titlereview__rating')
    ).order_by('-year', 'name')
    # ordering = ['-year']
    paginate_by = 5


class TitleDetailView(DetailView):
    model = Title


class TitleSearchView(ListView):
    model = Title
    template_name = 'tmdb/home.html'
    context_object_name = 'titles'

    def get_queryset(self):
        result = super(TitleSearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Title.objects.filter(Q(name__contains=query)
                                              | Q(titlecast__person__name__contains=query)
                                              | Q(titlecrew__person__name__contains=query))\
                .order_by('-year', 'name')
            result = postresult
        else:
            result = None
        return result


class MovieListView(ListView):
    model = Title
    template_name = 'tmdb/home.html'
    context_object_name = 'titles'
    queryset = Title.objects.filter(type__exact='Movie').annotate(
        avg_rating=Avg('titlereview__rating')
    ).order_by('-year', 'name')
    paginate_by = 5


class ShowListView(ListView):
    model = Title
    template_name = 'tmdb/home.html'
    context_object_name = 'titles'
    queryset = Title.objects.filter(type__exact='Show').annotate(
        avg_rating=Avg('titlereview__rating')
    ).order_by('-year', 'name')
    paginate_by = 5


class LatestListView(ListView):
    model = Title
    template_name = 'tmdb/home.html'
    context_object_name = 'titles'
    queryset = Title.objects.filter(year__exact=timezone.now().year).annotate(
        avg_rating=Avg('titlereview__rating')
    ).order_by('name')
    paginate_by = 5


class TopRatedListView(ListView):
    model = Title
    template_name = 'tmdb/home.html'
    context_object_name = 'titles'
    queryset = Title.objects.all().annotate(
        avg_rating=Avg('titlereview__rating')
    ).order_by('-avg_rating', 'name')[:5]
    paginate_by = 5


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = TitleReview
    fields = ['rating', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user

        title = self.get_object()
        form.instance.title = title
        return super().form_valid(form)


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TitleReview
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
    model = TitleReview
    success_url = '/'

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True
        return False
