from django.db import models

from django.contrib.auth.models import User
from django.core.validators import URLValidator

from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField, USZipCodeField
from PIL import Image

#from users.models import User

class Genre(models.Model):
    '''movie genres'''
    text = models.CharField(max_length = 20)
    def __str__(self):
        '''string representation of the model'''
        return self.text.title()
    class Meta:
        ordering = ('text',)

class PGRating(models.Model):
    '''types of pg rating'''
    text = models.CharField(max_length = 10)
    def __str__(self):
        '''string representation of the model'''
        return self.text

class Person(models.Model):
    '''movie people'''
    first_name  = models.CharField(max_length = 20)
    last_name   = models.CharField(max_length = 20)
    dob         = models.DateField(blank=True)
    image       = models.ImageField(upload_to = 'media')
    city        = models.CharField(max_length = 20, blank=True)
    state       = USStateField(choices=STATE_CHOICES)
    country     = models.CharField(max_length = 3, default='USA', editable=False)
    def __str__(self):
        return self.first_name.title() + ' ' +self.last_name.title()
    class Meta:
        ordering = ('first_name',)


class Movie(models.Model):
    '''Info about a movie'''
    title       = models.CharField(max_length = 100)
    release_dt  = models.DateField()
    genre       = models.ManyToManyField(Genre, related_name='genre')
    pg_rating   = models.ForeignKey(PGRating, on_delete = models.CASCADE)
    length      = models.SmallIntegerField('Length (mins):')
    plot        = models.TextField()
    actors      = models.ManyToManyField(Person, related_name='actors')
    writers     = models.ManyToManyField(Person, related_name='writers')
    directors   = models.ManyToManyField(Person, related_name='directors')
    photo       = models.ImageField(upload_to = 'media')
    trailer     = models.CharField('Trailer (youtube video id)', max_length = 11)
    def __str__(self):
        '''return a string representation of the model'''
        #return '%s %s' % (self.title.title(), self.genre)
        return self.title.title()
    class Meta:
        ordering = ('title',)


class Review(models.Model):
    '''User reviews for a movie'''
    movie       = models.ForeignKey(Movie, on_delete = models.CASCADE)
    text        = models.TextField()
    user        = models.ForeignKey(User, on_delete = models.CASCADE)
    review_dt   = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        '''return a string representation of the model'''
        return self.text[:50] + '...'

class Watchlist(models.Model):
    '''User movie watchlist'''
    user        = models.OneToOneField(User, on_delete= models.CASCADE)
    movie       = models.ManyToManyField(Movie, related_name='watchlist')
    def __str__(self):
        '''return a string representation of the model'''
        return str(self.id)+','+str(self.user.id)
