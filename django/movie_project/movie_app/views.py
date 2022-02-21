from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from .models import Movie


# Create your views here.


def show_all_movies(request):
    # movies = Movie.objects.all()
    # movies = Movie.objects.order_by('-rating')[:5]
    # movies = Movie.objects.order_by('rating', '-budget')
    # movies = Movie.objects.order_by(F('year').desc(nulls_last=True))  # nulls will be showed last
    movies = Movie.objects.annotate(true_bool=Value(True),
                                    false_bool=Value(False),
                                    str_field=Value('hello'),
                                    int_field=Value(123),
                                    new_budget=F('budget') + 100
                                    ).annotate(new_field=F('rating') + F('year'))
    agg = movies.aggregate(Avg("budget"), Max("rating"), Min("rating"), Count('name'))
    # for movie in movies:
    #     movie.save()
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg,
        'total': movies.count()
    })


def show_one_movie(request, slug_movie: str):
    # movie = Movie.objects.get(id=id_movie)
    # movie = get_object_or_404(Movie, id=id_movie)
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {'movie': movie})


def keanu(request):
    data = {
        'year_born': 1964,
        'city_born': 'Beirut',
        'movie_name': 'Point Break'
    }
    return render(request, 'movie_app/keanu.html', context=data)


def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'movie_app/guinnessworldrecords.html', context=context)