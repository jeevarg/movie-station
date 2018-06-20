from django.contrib import admin

# Register your models here.
from . models import Genre, PGRating, Person, Movie, Review, Watchlist

admin.site.register(Genre)
admin.site.register(PGRating)
admin.site.register(Person)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Watchlist)
