from django.shortcuts import render
import requests

def movies(request):

    response = requests.get('https://yts.am/api/v2/list_movies.json?order_by=desc&sort_by=seeds')
    movies = response.json()
    titles=[]
    for k,element in enumerate(movies['data']['movies']):
        titles.append(element['title'])

    response = requests.get('https://yts.am/api/v2/list_movies.json?')
    shows = response.json()
    series_titles=[]
    for k,element in enumerate(movies['data']['movies']):
        titles.append(element['title'])

    return render(request, 'pctime.html',{
    'titles':titles
    })
