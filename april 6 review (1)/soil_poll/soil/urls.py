from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('/dashboard', views.dashboard,name='dashboard'),
    path('/about',views.about,name='about'),
    path('predict/', views.predict_soil,name='predict'),
    path('recommend-crops/', views.recommend_crops, name='recommend_crops'),
    path('prediction/', views.prediction_page, name='prediction_page'),
]