from django.urls import path
from . import views
from django.urls import include

urlpatterns =[
    path('', views.HomePageView, name='kotisivu'),
    path('books/', include('books.urls')),
    path('Api/', include('Api.urls')),
]