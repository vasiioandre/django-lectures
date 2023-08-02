from django.urls import path
from . import views

#register the app namespace
app_name = 'my_app'

urlpatterns = [
    path('', views.example_view),
    path('variable/', views.variable_view),
    path('page1/', views.page1_view, name='page1'),
    path('page2/', views.page2_view, name='page2'),
    path('inherit/', views.inheritance_example)
]