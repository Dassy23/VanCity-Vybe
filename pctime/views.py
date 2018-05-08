from django.shortcuts import render
import requests

def movies(request):
    response = requests.get('https://yts.am/api/v2/list_movies.json?sort=seeds&NOTdate_added')
    movies = response.json()
    titles=[]
    for k,element in enumerate(movies['data']['movies']):
        titles.append(element['title'])
    return render(request, 'pctime.html',{
    'titles':titles
    })
