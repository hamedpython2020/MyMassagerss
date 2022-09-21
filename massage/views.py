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
        return render(request, 'massage/post.html', context)

############################################



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
    post = list(Post.objects.filter(prof=request.user.profile))
    count = Post.objects.filter(prof=request.user.profile).count()
    section = count // 3
    g = []
    l = []
    n = []
    for i in range(1, section + 2):
        l = []
        g = []
        l.append(i)
        for s in range(3):
            if len(post) == 2:
                g.append(post[0])
                g.append(post[1])
                break
            elif len(post) == 1:
                g.append(post[0])
                break
            g.append(post[s])
            if s == 2:
                break
            pass
        for s in range(3):
            if len(post) == 0:
                break
            post.remove(post[0])
        l.append(tuple(g))
        n.append(tuple(l))
        if len(post) == 0:
            break
        pass

    context = {
        'base': n,
        "post": post,
        "section": section
    }
    return render(request, "massage/mypost.html", context)
############################################
