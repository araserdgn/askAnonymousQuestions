from django.urls import path
from .views import*

urlpatterns = [
    path('register/',userRegister,name='register'),
    path('login/',userLogin,name='login'),
    path('logout/',userLogout,name='logout'),
    path('profil/',profil,name='profil'),
    path('update/',profil_update,name='profil_update'),
]