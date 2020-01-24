from django.http import HttpResponseRedirect
from Ghost_Post.models import Post
from django.shortcuts import get_object_or_404, render
from Ghost_Post.forms import PostForm, DeleteForm
from django.contrib import messages
from django.urls import reverse
import random
import string


def generateRandomString():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(6))


def index(request):

    sort_by = request.GET.get('sort', 'dateSubmitted')
    latest_posts = Post.objects.order_by(sort_by)
    is_boast_param = request.GET.get('isBoast', '')
    if is_boast_param != '':
        latest_posts = Post.objects.filter(isBoast=is_boast_param).order_by(sort_by)
    context = {
        'latest_posts': latest_posts
    }
    return render(request, 'index.html', context)


def post_new(request):
    return render(request, 'postForm.html')


# TODO replace args "something" with post id
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            body = form.cleaned_data
            p = Post(isBoast=body['isBoast'], content=body['content'], secretKey=generateRandomString())
            p.save()
            context = {'secret': p.secretKey}
            return render(request, 'success.html', context)

    context = {'form': PostForm()}
    return render(request, 'postForm.html', context)


def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post, 'form': DeleteForm}
    if request.method == "POST":
        form = DeleteForm(request.POST)
        if form.is_valid():
            body = form.cleaned_data
            post = Post.objects.get(id=post_id)
            if post.secretKey == body['secret']:
                post.delete()
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.add_message(request, messages.INFO, 'Incorrect code')
    return render(request, "post.html", context)


def post_upVote(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.upVotes += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_Referer', '/'))


def post_downVote(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.downVotes += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_Referer', '/'))


