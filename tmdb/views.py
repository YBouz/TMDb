from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView

from .forms import ReviewForm
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
    template_name = 'tmdb/title_list.html'
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
    template_name = 'tmdb/title_list.html'
    context_object_name = 'titles'

    def get_queryset(self):
        result = super(TitleSearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Title.objects.filter(Q(name__contains=query)
                                              | Q(titlecast__person__name__contains=query)
                                              | Q(titlecrew__person__name__contains=query)) \
                .order_by('-year', 'name')
            result = postresult
        else:
            result = None
        return result


class MovieListView(ListView):
    model = Title
    template_name = 'tmdb/title_list.html'
    context_object_name = 'titles'
    queryset = Title.objects.filter(type__exact='Movie').annotate(
        avg_rating=Avg('titlereview__rating')
    ).order_by('-year', 'name')
    paginate_by = 5


class ShowListView(ListView):
    model = Title
    template_name = 'tmdb/title_list.html'
    context_object_name = 'titles'
    queryset = Title.objects.filter(type__exact='Show').annotate(
        avg_rating=Avg('titlereview__rating')
    ).order_by('-year', 'name')
    paginate_by = 5


class LatestListView(ListView):
    model = Title
    template_name = 'tmdb/title_list.html'
    context_object_name = 'titles'
    queryset = Title.objects.filter(year__exact=timezone.now().year).annotate(
        avg_rating=Avg('titlereview__rating')
    ).order_by('name')
    paginate_by = 5


class TopRatedListView(ListView):
    model = Title
    template_name = 'tmdb/title_list.html'
    context_object_name = 'titles'
    queryset = Title.objects.all().annotate(
        avg_rating=Avg('titlereview__rating')
    ).order_by('-avg_rating', 'name')[:5]
    paginate_by = 5


@login_required
def createReview(request, titlePK):
    review = TitleReview(author_id=request.user.pk, title_id=titlePK)
    # print(request.user.pk, titlePK)
    form = ReviewForm(instance=review)
    if request.method == 'POST':
        # print('Print Post: ', request.POST)
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('title-detail', titlePK)

    context = {'form': form}
    return render(request, 'tmdb/titlereview_form.html', context)


@login_required
def updateReview(request, titlePK, pk):
    review = TitleReview.objects.get(id=pk)
    form = ReviewForm(instance=review)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('title-detail', titlePK)

    context = {'form': form}
    return render(request, 'tmdb/titlereview_form.html', context)


@login_required
def deleteReview(request, titlePK, pk):
    review = TitleReview.objects.get(id=pk)
    if request.method == 'POST':
        review.delete()
        return redirect('title-detail', titlePK)

    context = {'item': review}
    return render(request, 'tmdb/delete.html', context)
