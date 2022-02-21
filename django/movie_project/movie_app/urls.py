from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movies),
    path('movie/keanu', views.keanu),
    path('worldrecords', views.get_guinness_world_records),
    # path('movie/<int:id_movie>', views.show_one_movie, name='movie-detail'),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
]
