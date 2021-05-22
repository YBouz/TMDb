from django.contrib import admin
from .models import Title, Genre, Person, Production, TitleGenre, TitleCast, TitleCrew, TitleProduction, TitleReview


# Customize


# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'rating', 'date_posted']
    list_filter = ['date_posted']
    search_fields = ['author', 'title']


admin.site.register(TitleReview, ReviewAdmin)

admin.site.register(Genre)
admin.site.register(Person)
admin.site.register(Production)


class GenreInline(admin.TabularInline):
    model = TitleGenre
    extra = 1
    verbose_name_plural = 'Genres'


class CrewInline(admin.TabularInline):
    model = TitleCrew
    extra = 1
    verbose_name_plural = 'Crew'
    ordering = ['person__name']


class CastInline(admin.TabularInline):
    model = TitleCast
    extra = 1
    verbose_name_plural = 'Cast'
    ordering = ['person__name']


class ProductionInline(admin.TabularInline):
    model = TitleProduction
    extra = 1
    verbose_name_plural = 'Production'


class ReviewInline(admin.TabularInline):
    model = TitleReview
    extra = 1
    verbose_name_plural = 'Reviews'


class TitleAdmin(admin.ModelAdmin):
    list_display = ['name', 'year']
    list_filter = ['year']
    search_fields = ['name', 'year']
    inlines = [GenreInline, CrewInline, CastInline, ProductionInline, ReviewInline]


admin.site.register(Title, TitleAdmin)
