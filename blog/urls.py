from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('quicknotes/', views.posts_list, name='post_list'),
    path('like/', views.like, name='like'),
    path('quicknotes/comments/', views.comments, name='comments'),
    path('quicknotes/<int:id>/<str:message>/', views.note, name='note'),
    path('quicknotes/<int:id>/', views.note, name='note'),
]
