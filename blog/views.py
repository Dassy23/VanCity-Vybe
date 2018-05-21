
from django.shortcuts import render, get_object_or_404
from .models import Post


def allposts(request):
    posts = Post.objects
    tags_dict = Post.objects.order_by('tag').values('tag').distinct()
    tags=[]
    for dict in tags_dict:
        for k,v in dict.items():
            tags.append(v)
    featured = Post.objects.order_by('pub_date')[:3]

    return render(request, 'blogs.html', {'posts':posts, 'tags':tags, 'featured':featured})

def postdetail(request, post_id):
    detailpost = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'detailpost':detailpost})
