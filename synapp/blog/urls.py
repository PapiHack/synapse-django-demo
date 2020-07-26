from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('add_post/', views.add_post, name="add_post"),
    path('edit_post/<int:id>', views.edit_post, name="edit_post"),
    path('post_detail/<int:id>', views.post_detail, name="post_detail"),
    path('delete_post/<int:id>', views.delete_post, name="delete_post"),
]
