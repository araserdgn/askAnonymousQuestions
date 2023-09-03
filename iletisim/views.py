from django.shortcuts import render,redirect
from .models import*
# Create your views here.
def iletisim(request):
    if request.method == 'POST':
        isim = request.POST['isim']
        email = request.POST['email']
        mesaj = request.POST['mesaj']

        iletilen = Contact(isim=isim , email=email , mesaj=mesaj)
        iletilen.save()
        return redirect('index')
    return render(request,'contact.html')