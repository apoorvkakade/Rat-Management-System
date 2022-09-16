from django.urls import path
from . import views
urlpatterns=[
    path('',views.home_function,name='home'),
    path('update/<str:specie_name>/<str:entry_date>',views.update,name='update'),



]