from django import template
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from post.models import Image, Stream, Tag
from post.forms import NewPostForm
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

@login_required
def PostDetails(request, post_id):
    post = get_object_or_404(Image, id=post_id)

    template = loader.get_template('post_detail.html')

    context = {
        'post': post,
    }

    return HttpResponse(template.render(context, request))

@login_required
def NewPost(request):
    user = request.user.id
    tags_objs = []

    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            caption = form.cleaned_data.get('caption')
            tags_form = form.cleaned_data.get('tags')

            tags_list = list(tags_form.split(','))

            for tag in tags_list:
                t, created = Tag.objects.get_or_create(title=tag) 
                tags_objs.append(t)

            p, created = Image.objects.get_or_create(picture=picture, caption=caption, user_id=user)
            p.tags.set(tags_objs)
            p.save()
            return redirect('index')

    else:
        form = NewPostForm()

    context = {
        'form': form,
    }

    return render(request, 'newpost.html', context)

