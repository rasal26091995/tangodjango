from django.urls import path
from ordix import views

app_name = 'ordix'

urlpatterns = [
    path('', views.index, name='index'),
]