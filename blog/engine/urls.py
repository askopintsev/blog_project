from django.urls import path

from . import views

app_name = 'engine'
urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('post/<int:post_id>', views.post_page, name='post'),
]
