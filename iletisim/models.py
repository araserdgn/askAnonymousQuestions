from django.db import models

# Create your models here.
class Contact(models.Model):
    isim = models.CharField(max_length=50, verbose_name="Kullanıcı adı: ",null=True)
    mesaj = models.TextField(max_length=50,verbose_name="Şikayet Mesajı: ",null=True)
    email = models.CharField(max_length=50, verbose_name="Email: ",null=True)

    def __str__(self):
        return f"{self.isim}"