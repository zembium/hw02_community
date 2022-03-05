from django.shortcuts import render, get_object_or_404
from .models import Post, Group

MAX_POSTS: int = 10


# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:MAX_POSTS]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


# Посты сообщества slug
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:MAX_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
