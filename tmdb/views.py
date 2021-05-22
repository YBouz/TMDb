from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Title, TitleReview


# Create your views here.
class TitleListView(ListView):
    model = Title
    template_name = 'tmdb/home.html'
    context_object_name = 'titles'
    ordering = ['-year']
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
            #postresult = Title.objects.filter(Q(name__contains=query) | Q(titlecrew__person__name__contains=query))
            postresult = Title.objects.filter(Q(name__contains=query))
            result = postresult
        else:
            result = None
        return result


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
