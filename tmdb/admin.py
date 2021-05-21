from django.contrib import admin
from .models import Movie, Genre, Person, Review


# Customize


# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Person)
admin.site.register(Review)
