from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

from . models import Movie, Genre, Person, Review, Watchlist
from datetime import datetime

def index(request):
    '''home page for movies which shows latest 10 movies in a carousel'''
    movies = Movie.objects.order_by('-release_dt')[:10]
    context = {'movies':movies}
    return render(request,'movies/index.html', context)


def latest_movies(request):
    '''shows latest 10 movies'''
    genres = Genre.objects.all()
    #latest_ten_movies = Movie.objects.order_by('-release_dt')[:10]
    movies = Movie.objects.order_by('-release_dt')[:10]
    context = {'movies':movies,'genres':genres}
    return render(request, 'movies/latest-movies.html', context)

def latest_movies_genre(request, id):
    '''filters the latest 10 movies by genre'''
    #genres = Genre.objects.all()
    result=[]
    movies = Movie.objects.order_by('-release_dt')[:10]
    for movie in movies:
        for genre in movie.genre.all():
            if genre.id == id:
                genre_text = genre.text
                result.append(movie)
                break
    context={'movies':result,'genre':genre_text}
    return render(request,'movies/latest-movies-genre.html',context)

def movies_by_genre(request, id):
    '''show all the movies by selected genre'''
    movies = Movie.objects.filter(genre__id=id)
    genre = Genre.objects.get(id=id)
    context={'movies':movies,'genre':genre}
    return render(request, 'movies/movies-by-genre.html',context)

def movies_years(request):
    '''displays the movies years'''
    movies = Movie.objects.all()
    years = []
    for movie in movies:
        years.append(movie.release_dt.year)
    unique_years = list(sorted(set(years)))
    print(unique_years)
    unique_years.reverse()
    context={'years':unique_years}
    return render(request,'movies/movies-years.html', context)

def year_movies(request,year):
    '''displays the movies from a particular year'''
    movies = Movie.objects.all()
    context={'movies':movies,'year':year}
    return render(request, 'movies/year-movies.html', context)

def born_today(request):
    '''displays the celebrities whose birthday is today'''
    persons = Person.objects.all()
    result=[]
    for person in persons:
        if person.dob.month == datetime.now().month and person.dob.day == datetime.now().day:
            result.append(
                {'first_name':person.first_name,
                'last_name':person.last_name,
                'dob':person.dob,
                'image':person.image.url,
                'city':person.city,
                'state':person.state,
                'country':person.country}
            )
    born_month_day = datetime.now().strftime('%m''-''%d')
    context={'persons':result,'born_month_day':born_month_day}
    return render(request, 'movies/born-today.html',context)

def latest_posters(request):
    '''displays the latest posters of all movies'''
    movies = Movie.objects.all()
    context={'movies':movies}
    return render(request, 'movies/latest-posters.html',context)

def movie_overview(request,id):
    '''displays the movie overview of a selected movie'''
    movie = Movie.objects.get(id=id)
    context = {'movie':movie}
    return render(request, 'movies/movie-overview.html', context)

def movie_plot(request,id):
    '''shows the movie plot'''
    movie = Movie.objects.get(id=id)
    context = {'movie':movie}
    return render(request, 'movies/movie-plot.html', context)

def movie_reviews(request,id):
    '''shows the movie reviews'''
    movie = Movie.objects.get(id=id)
    reviews = movie.review_set.all()
    context = {'reviews':reviews,'movie':movie}
    return render(request, 'movies/movie-reviews.html', context)

def movie_cast_crew(request,id):
    '''displays the movie cast and crew'''
    movie = Movie.objects.get(id=id)
    context = {'movie':movie}
    return render(request, 'movies/movie-cast-crew.html', context)

def person_bio(request,id):
    '''displays the bio-info of a person'''
    person = Person.objects.get(id=id)
    context={'person':person}
    return render(request, 'movies/person-bio.html',context)

def watch_list(request):
    '''displays the watchlist of a logged in user'''
    if request.user.is_authenticated:
        try:
            watchlist = Watchlist.objects.get(user__id=request.user.id)

        except Exception as e:
            watchlist = 0
    else:
        return render(request, 'movies/watch-list1.html', )
    context = {'watchlist':watchlist}
    return render(request,'movies/watch-list.html', context)

def popular_movie_list(request):
    '''displays the popular movie list from the database'''
    movies = Movie.objects.order_by('release_dt')[:10]
    context = {'movies':movies}
    return render(request,'movies/popular-movie-list.html',context)

def watchlist_add(request,movie_id):
    '''create/update the watchlist for logged in user'''
    try:
        Watchlist.objects.create(user=request.user.id, movie=movie_id)
    except Exception as e:
        pass
    else:
        return render(request,'movies/popular-movie-list.html',context)

def search_data(request):
    '''search the database for a movie based on the text input'''
    if request.method == 'POST':
        search = request.POST['searchdata']
        if search:
            result = Movie.objects.filter(title__iexact=search)
            if result:
                context = {'movies':result}
            else:
                context = {'movies':0}
            return render(request,'movies/search-data.html',{'movies':result})
        else:
            return  HttpResponseRedirect(reverse('movies:index'))
    return render(request,'movies/index.html')
