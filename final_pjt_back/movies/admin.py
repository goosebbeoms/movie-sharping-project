from django.contrib import admin
from .models import Movie, Actor, Genre, HashTag, Review

# Register your models here.
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(HashTag)
admin.site.register(Review)