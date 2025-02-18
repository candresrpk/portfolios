from django.urls import path
from . import views

app_name = 'honey'


urlpatterns = [
    path('', views.home_view, name='home'),
    path('/create', views.create_view, name='create'),

]
