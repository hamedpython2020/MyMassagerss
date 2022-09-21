from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
#################################################
from account.forms import Signup_form, profil_form, name
from account.models import Profile
import time
from massage.models import Post


def index(request):
    user = request.user
    if user.is_authenticated:
        prof = Profile.objects.get(user=request.user)
        post_number = Post.objects.filter(prof=prof).count()
        posts = Post.objects.all().order_by("share_date")
        context = {
            "post_num": post_number,
            "posts": posts
        }
    else:
        posts = Post.objects.all().order_by("share_date")
        context = {
            "posts": posts
        }
    return render(request, "Accounts/index.html", context)
#################################################


def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is None:
            context = {
                'username': username,
                'error': 'موجود نیست'
            }
        else:
            login(request, user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))
            else:
                return HttpResponseRedirect(reverse(viewname='index'))
            pass
        pass
    else:
        context = {}
    return render(request, "Accounts/login.html", context)
#################################################


def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(viewname='index'))
#################################################


def Signup(request):
    if request.user.is_authenticated:
        context = {
            'errors': 'ابتدا لاگ اوت کنید',
            'page': 'logout',
            'order': 'logout'
        }
        return render(request, 'Accounts/errors.html', context)
    else:
        if request.method == 'POST':
            user = Signup_form(request.POST)
            if user.is_valid():
                user.save()
                my_username = user.cleaned_data['username']
                my_user = User.objects.get(username=my_username)
                login(request, my_user)
                return HttpResponseRedirect(reverse('account:profile_create'))
            else:
                context = {
                    'error': user.error_class,
                    'user': user
                }
        else:
            # Just load the empty form
            user = Signup_form()
            context = {
                'user': user
            }
        return render(request, 'Accounts/signup.html', context)
    pass
#################################################


@login_required
def Profilecreat(request):
    user = request.user
    if user.profile is None:
        if request.method == 'POST':
            prof = profil_form(request.POST)
            names = name(request.POST)
            if prof.is_valid() and names.is_valid():
                profile = prof.save(commit=False)
                profile.user = request.user
                profile.birth_date = prof.cleaned_data['Birth_date']
                profile.save()
                user.first_name = names.cleaned_data['first_name']
                user.last_name = name.cleaned_data['last_name']
                user.save()
                return HttpResponseRedirect(reverse('index'))
            context = {
                'prof': prof,
                'names': names
            }
        else:
            prof = profil_form()
            names = name()
            context = {
                'prof': prof,
                'names': names
            }
        return render(request, 'Accounts/profile_creat.html', context)
    else:
        return HttpResponseRedirect(reverse(viewname='index'))

#################################################


@login_required
def Myprofile(request, profile_id):
    user = request.user
    prof = Profile.objects.get(pk=profile_id)
    context = {
        'prof': prof
    }
    return render(request, 'Accounts/profile.html', context)

#################################################


@login_required
def edit_profile(request, profile_id):
    if profile_id == request.user.profile.id and request.user.profile.clean():
        if request.method == 'POST':
            prof = profil_form(request.POST, request.FILES, instance=request.user.profile)
            if prof.is_valid():
                prof.save()
                return HttpResponseRedirect(reverse(viewname='myprofile'))
            context = {
                'prof': prof
            }
        else:
            prof = profil_form(request.FILES, instance=request.user.profile)
            context = {
                'prof': prof
            }
            return render(request, 'Accounts/profile_creat.html', context)
        pass
    else:
        context = {
            "errors": "پروفایل مورد نظر در دسترس نیست"
        }
        return render(request, "Accounts/errors.html", context)
    pass

#################################################

