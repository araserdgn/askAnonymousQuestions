from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):

    owner= models.OneToOneField(User , on_delete=models.CASCADE,verbose_name="Kullanici",null=True)
    isim = models.CharField(max_length=100,verbose_name="Kullanıcı İsmi",null=True)
    nickname = models.CharField(max_length=100,verbose_name="Kullanıcı nickname",null=True)
    email = models.CharField(max_length=100, verbose_name="Kullanıcı email",null=True)
    resim = models.ImageField(upload_to='profil_resimler/',null=True)

    def __str__(self):
        return f"{self.nickname}"
    

