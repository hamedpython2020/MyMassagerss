from django.urls import path

from account import views

app_name = 'account'

urlpatterns = [

    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('signup/', views.Signup, name='signup'),
    path('profile/create', views.Profilecreat, name='profile_create'),
    path('profile/<int:profile_id>', views.Myprofile, name='myprofile'),
    path('profile/<int:profile_id>/edit', views.edit_profile, name='edit_profile'),

]