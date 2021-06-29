from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('quicknotes/', views.quicknote, name='quicknote'),
    path('post-like/', views.like, name='post-like'),
    path('quicknotes<int:id>/comments/', views.comments, name='comments'),
    path('quicknotes/<int:id>/<str:message>/', views.note, name='note'),
    path('quicknotes/<int:id>/', views.note, name='note'),
]
