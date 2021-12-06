from django.contrib import admin
from . models import Genre
from . models import Category
from . models import MoviesLink


admin.site.register(Genre)
admin.site.register(MoviesLink)
admin.site.register(Category)