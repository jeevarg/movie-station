from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'movies'

urlpatterns = [
    path('',views.index, name='index'),
    path('latest-movies/', views.latest_movies, name='latest-movies'),
    #url(r'^latest-movies/(?P<id>\d+)$', views.latest_movies_genre, name='latest-movies-genre'),
    path('latest-movies/<int:id>/', views.latest_movies_genre, name='latest-movies-genre'),
    path('movies-by-genre/<int:id>/', views.movies_by_genre, name='movies-by-genre'),
    path('movies-years/', views.movies_years, name='movies-years'),
    path('year-movies/<int:year>/', views.year_movies, name='year-movies'),
    path('born-today/', views.born_today, name='born-today'),
    path('latest-posters/', views.latest_posters, name='latest-posters'),
    path('movie-overview/<int:id>/', views.movie_overview, name='movie-overview'),
    path('movie-plot/<int:id>/', views.movie_plot, name='movie-plot'),
    path('movie-reviews/<int:id>/', views.movie_reviews, name='movie-reviews'),
    path('movie-cast-crew/<int:id>/',views.movie_cast_crew, name='cast-crew'),
    path('person-bio-data/<int:id>/',views.person_bio, name='person-bio-data'),
    path('watch-list/', views.watch_list, name='watch-list'),
    path('popular-movie-list/', views.popular_movie_list, name='popular-movie-list'),
    path('watchlist-add/<int:movie_id>/', views.watchlist_add, name='watchlist-add'),
    path('search-data/', views.search_data, name='search-data'),

]
