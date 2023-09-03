from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Kategoriler(models.Model):
    kategori=models.CharField(max_length=30,verbose_name="Kategori Adı:",)

    def __str__(self):
        return (self.kategori)
    


class Sorular(models.Model):
    username=models.CharField(max_length=20,verbose_name="Kullanıcı Adı")
    soru=models.TextField()
    isAnonim= models.BooleanField(default=False)
    kullanici = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Kategoriler,default=1, on_delete=models.SET_DEFAULT,related_name="Sorular") #! CASCADE , bir kategory silince bağlı olduklarının hepsini siler yani    
    #! related = sorgularda kurslar dediğinde artık kategoryde ona ait olanları direkt alabilirsn 
    categories = models.ManyToManyField(Kategoriler)

    def __str__(self):
        return f"{self.username}"
    
class Cevaplar(models.Model):
    username=models.CharField(max_length=20,verbose_name="Admin kullanıcı",null=True)
    sorular = models.ForeignKey(Sorular,on_delete=models.CASCADE)
    cevap=models.TextField()

    def __str__(self):
        return self.cevap
    

