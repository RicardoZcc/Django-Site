from django.urls import path
from base import views


urlpatterns = [
    path('', views.home, name='hello_world'),
    path("<int:pk>/", views.projetopage, name="projetopage"),
    path("blog/", views.blog_index, name="blog_index"),
    path("blog/<categoria>/", views.blog_categoria, name="blog_categoria"),
    path("blog/post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path('henryjames/', views.henryjames, name='henryjames'),
]