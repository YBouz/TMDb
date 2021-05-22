from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Title(models.Model):
    TYPES = [
        ('Movie', 'Movie'),
        ('Show', 'Show')
    ]
    type = models.CharField(max_length=10, choices=TYPES, default='Movie')
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(default='default_poster.jpg', upload_to='title_posters')
    trailer_url = models.CharField(max_length=250)
    year = models.IntegerField()
    runtime = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('title-detail', kwargs={'pk': self.pk})


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'


class TitleGenre(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} -- {self.genre}'


class Person(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    dob = models.DateField()

    def __str__(self):
        return f'{self.name}'


class TitleCast(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    character = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.person} -- {self.title}'


class TitleCrew(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    ROLES = [
        ('Director', 'Director'),
        ('Producer', 'Producer'),
        ('Executive Producer', 'Executive Producer'),
        ('Screen Writer', 'Screen Writer'),
        ('Creator', 'Creator'),
    ]
    role = models.CharField(max_length=50, choices=ROLES, default='Director')

    def __str__(self):
        return f'{self.person} -- {self.title}'


class Production(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class TitleProduction(models.Model):
    company = models.ForeignKey(Production, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.company} -- {self.title}'


class TitleReview(models.Model):
    STARS = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], choices=STARS, default=5)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} - ({self.date_posted})'
