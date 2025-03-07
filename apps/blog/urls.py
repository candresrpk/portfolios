from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('post_detail/<slug:slug>', views.PostDetailView.as_view(), name='detail'),

]
