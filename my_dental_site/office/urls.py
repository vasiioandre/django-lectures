from django.urls import path
from . import views

urlpatterns = [
    # domain.com/office  ---> list of all the patients
    path('', views.list_patients, name='list_patients')
]