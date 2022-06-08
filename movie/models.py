from django.db import models

# Create your models here.

class Actor(models.Model):
    first_name      = models.CharField(max_length=45)
    last_name       = models.CharField(max_length=45)
    date_of_birth   = models.DateField()
    movies          = models.ManyToManyField('Movie',
                                             db_table='actor_movie',
                                             through='ActorMovie',
                                             through_fields=('actor','movie')
                                             )

    class Meta:
        db_table = 'actors'

class Movie(models.Model):
    title           = models.CharField(max_length=45)
    release_date    = models.DateField()
    running_time    = models.IntegerField()
    class Meta:
        db_table = 'movies'

class ActorMovie(models.Model):
    actor          = models.ForeignKey()
    movie          = models.ForeignKey()