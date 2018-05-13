from django.shortcuts import render
import requests

def movies(request):

    response = requests.get('https://yts.am/api/v2/list_movies.json?sort_by=date_added&sort_by=year&limit=20&minimum_rating=7&order_by=desc')
    movies = response.json()
    titles=[]
    ids=[]
    for k,element in enumerate(movies['data']['movies']):
        titles.append(element['title'])
        ids.append(element['id'])
    img_ids='&'.join(str(v) for v in ids)
    request_string= 'https://yts.am/api/v2/movie_details.json?movie_id='+ img_ids + '&with_images=true'
    image_response=requests.get(request_string)
    img = image_response.json()
    movie_covers=[]
    for k,element in enumerate(movies['data']['movies']):
        movie_covers.append(element['medium_cover_image'])
    movie_info=zip(titles,movie_covers)
    return render(request, 'pctime.html',{
    'movie_info':movie_info,
    })
