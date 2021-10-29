from django.shortcuts import get_object_or_404, render
from .models import Post, Group


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.group_posts.all().order_by('-pub_date')[:10]
    text = 'текст'
    context = {
        'text': text,
        'group': group,
        'posts': posts
    }
    return render(request, 'posts/group_list.html', context)
