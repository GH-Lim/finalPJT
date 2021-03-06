from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
    survey = models.BooleanField(default=False)
    genre = models.CharField(max_length=150, default='')


class Genre(models.Model):
    genreNm = models.CharField(max_length=150)


class Actor(models.Model):
    name = models.CharField(max_length=50)


class Director(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    movieCd = models.CharField(max_length=20)
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.CharField(max_length=150)
    openDt = models.CharField(max_length=12)
    audiAcc = models.IntegerField()
    score = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )
    directors = models.ManyToManyField(Director, related_name="movies")
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")
    like_users = models.ManyToManyField(User, related_name="like_movies")
    backgroundImage = models.CharField(max_length=150)
    

class Comment(models.Model):
    content = models.CharField(max_length=150)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
