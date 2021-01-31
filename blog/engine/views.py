from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse

from .models import Post, Comment
from .forms import CommentForm


def index_page(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 10)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)

    context = {
        'posts': page_posts
    }
    return render(request, "engine/pages/index.html", context)


def post_page(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comments
    new_comment = None
    comment_form = None

    if request.method == 'POST':
        # Комментарий был опубликован
        form_data = CommentForm(data=request.POST)
        if form_data.is_valid():
            new_comment = form_data.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse('engine:post', args=[post.id]))
    else:
        comment_form = CommentForm()

    context = {'post': post,
               'comments': comments,
               'new_comment': new_comment,
               'comment_form': comment_form
               }

    return render(request, "engine/pages/post.html", context)
