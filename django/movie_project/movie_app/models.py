from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):  # this method definition doesn't have effect to DB structure, so it won't detect any changes
        return f'{self.first_name} {self.last_name}'


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
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    # any of these changes will affect DB structure, so makemigrations is required
    year = models.IntegerField(null=True, blank=True)  # allows null registers in this field
    budget = models.IntegerField(default=1000000, validators=[MinValueValidator(0)])  # default value if not set
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)  # default is only for new register
    slug = models.SlugField(default='', null=False, db_index=True)  # db_index -> searching in DB is faster
    # director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True)  # many to many, cannot delete
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)  # many to many, will delete
    # director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)  # many to many, will set null

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        # return reverse('movie-detail', args=[self.id])
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):  # this method definition doesn't have effect to DB structure, so it won't detect any changes
        return f'{self.name} | {self.rating}%'
