from django.urls import path , include
from . import views

urlpatterns = [
    path('', include('allauth.urls')),
    path('sign_in' , views.sign_in , name = 'sign_in'),
    path('sign_up' , views.sign_up , name = 'sign_up'),
    path('sign_out' , views.sign_out , name = 'sign_out'),
]

