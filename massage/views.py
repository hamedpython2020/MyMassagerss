from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.template import loader
from django.urls import reverse
from massage.forms import newpost
from massage.models import Post, viewer


############################################

@login_required
def Post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    prof = request.user.profile
    try:
        view = viewer.objects.get(prof=prof, post=post)
    except:
        view = None
    if view is None and prof != post.prof:
        view = viewer.objects.create(post=post, prof=prof)
        post.views += 1
        pass
    if request.method == 'POST':
        comment = request.POST.get('comment')
        like = request.POST.get('like')
        if view is not None:
            view.comment = comment
            view.save()
        if like is True:
            post.like += 1
        post.save()
        context = {
            'post': post
        }
        return HttpResponseRedirect(reverse(viewname='massage:post_list'))
    else:
        if view != None:
            view.save()
            post.save()
        context = {
            'post': post
        }
        return render(request, 'massage/posts_view.html', context)

############################################


def Post_list(request):
    posts = Post.objects.all().order_by('share_date')
    context = {
        'posts': posts,
    }
    return render(request, 'massage/posts_list.html', context)

############################################


def Post_data(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    data = post.data
    context = {
        'data': data,
        'post': post
    }
    return render(request, 'massage/post_data.html', context)

############################################


@login_required
def New_post(request):
    if request.method == 'POST':
        post = newpost(request.POST, request.FILES)
        if post.is_valid():
            new_post = post.save(commit=False)
            new_post.prof = request.user.profile
            new_post.save()
            return HttpResponseRedirect(reverse('massage:Post_view', kwargs={'post_id': new_post.pk}))

        context = {
            'post': post
        }
    else:
        post = newpost()
        context = {
            'post': post
        }
    return render(request, 'massage/newpost.html', context)

############################################


def Mypost(request):
    post = Post.objects.filter(prof=request.user.profile)
    context = {
        "post": post
    }
    return render(request, "massage/mypost.html", context)
############################################
