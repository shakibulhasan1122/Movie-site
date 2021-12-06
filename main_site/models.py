from django.db import models
from django.utils import timezone

class Genre(models.Model):
    genre=models.CharField(max_length=100)

    def __str__(self):
        return self.genre

class Category(models.Model):
    category=models.CharField(max_length=100)

    def __str__(self):
        return self.category

class MoviesLink(models.Model):
    movie_title=models.CharField(max_length=100)
    link=models.TextField()
    image=models.ImageField(null=True, blank=True)
    add_time=models.DateTimeField(default=timezone.now)
    gen=models.ForeignKey(
     'Genre',
     on_delete=models.CASCADE,
     default=None
     )
    category=models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        default=None
        )
    def __str__(self):
        return self.movie_title    