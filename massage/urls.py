from django.urls import path
from massage import views

app_name = 'massage'

urlpatterns = [
    path('post/<int:post_id>/', views.Post_view, name='Post_view'),
    path('post/list/', views.Post_list, name='post_list'),
    path('post/data/<int:post_id>/', views.Post_data, name='post_data'),
    path('post/new/', views.New_post, name='new_post'),
    path('post/mine/', views.Mypost, name='mypost'),


]