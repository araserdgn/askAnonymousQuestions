from django.urls import path
from .views import*

urlpatterns = [
    path('',index,name='index'),
    path("about/",about,name="about"),
    path("sorular/",questionP,name="sorular"),
    path("create-ask/",create_ask,name="create_ask"),
    path("search/",arama,name="search"),
    path("answer/",create_answer,name="create_answer"),
    path("kategori-soru/<str:kategori>",getCategory,name="kategori_soru"),
]