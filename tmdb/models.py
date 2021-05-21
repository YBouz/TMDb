from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(default='default_poster.jpg', upload_to='movie_posters')
    trailer_url = models.CharField(max_length=250)
    year = models.IntegerField()
    directors = models.CharField(max_length=250)
    production = models.CharField(max_length=100)
    genres = models.CharField(max_length=50)
    runtime = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'pk': self.pk})


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Person(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    dob = models.DateField()

    def __str__(self):
        return f'{self.name}'


class Review(models.Model):
    rating = models.IntegerField()
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} - {self.movie} ({self.date_posted})'

    # def get_absolute_url(self):
    #     return reverse('review-create', kwargs={'pk': self.pk})
        # not sure about this
