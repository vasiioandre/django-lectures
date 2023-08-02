from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index,name='index') #/my_apps --> PROJECT urls.py
    # path('', views.simple_view),

    # path('sports/', views.sports_page),
    # path('finance/', views.finance_page)

    # path('<int:num_page>', views.num_page_view),

    # path('<str:topic>', views.news_view),
    # path('<int:num1>/<int:num2>', views.add_view),

    # path('<str:topic>/', views.news_view, name='topic-page'),
    
    path('', views.simple_view) # domain.com/first_app
]