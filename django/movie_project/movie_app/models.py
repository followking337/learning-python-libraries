from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


# from movie_app.models import Movie
class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollars'),
        (RUB, 'Rubles')
    ]
    # id --> will be created automatically by ORM
    name = models.CharField(max_length=40)
    rating = models.IntegerField()  # any of these changes will affect DB structure, so makemigrations is required
    year = models.IntegerField(null=True, blank=True)  # allows null registers in this field
    budget = models.IntegerField(default=1000000)  # default value if not set
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)  # default is only for new register
    slug = models.SlugField(default='', null=False, db_index=True)  # db_index -> searching in DB is faster

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        # return reverse('movie-detail', args=[self.id])
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):  # this method definition doesn't have effect to DB structure, so it won't detect any changes
        return f'{self.name} | {self.rating}%'
