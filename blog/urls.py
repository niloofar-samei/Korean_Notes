from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('post-like/', views.like, name='post-like'),
    path('<int:id>/comments/', views.comments, name='comments'),
    path('<int:id>/<str:message>/', views.note, name='note'),
    path('<int:id>/', views.note, name='note'),
]
