from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from post.models import Image, Stream
from django.template import loader

# Create your views here.
@login_required
def index(request):
    '''
    this is a view function that renders our homepage
    '''
    user = request.user
    posts = Stream.objects.filter(user=user)

    group_ids = []

    for post in posts:
        group_ids.append(post.post_id)

    post_items = Image.objects.filter(id__in=group_ids).all().order_by('-posted')

    template = loader.get_template('index.html')

    context = {
        'post_items': post_items,
    }

    return HttpResponse(template.render(context, request))