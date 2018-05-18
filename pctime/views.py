from django.shortcuts import render
import requests

def movies(request):

    response = requests.get('https://yts.am/api/v2/list_movies.json?sort_by=date_added&sort_by=year&limit=20&minimum_rating=7&order_by=desc&limit=21')
    movies = response.json()
    titles=[]
    movie_covers=[]
    summary=[]
    for k,element in enumerate(movies['data']['movies']):
        titles.append(element['title'])
        movie_covers.append(element['medium_cover_image'])
        summary.append(element['summary'])

    movie_info=zip(titles,movie_covers,summary)
    return render(request, 'pctime.html',{
    'movie_info':movie_info,
    })
