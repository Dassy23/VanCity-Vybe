from django.shortcuts import render
import requests

def movies(request):
    response = requests.get('https://yts.am/api/v2/movie_details.json?movie_id=15&with_images=true')
    movies = response.json()
    return render(request, 'pctime.html', {
        'movies': movies,
    })
