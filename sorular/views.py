from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from sorular.models import *
from user.models import *


# Create your views here.
def index(request):
    kategoriler = Kategoriler.objects.all()
    kullanicilar = Profile.objects.all()
    son_kategori = Kategoriler.objects.last()
    son_kullanıcı = Profile.objects.last()
    # prof=Profile.objects.get(owner=request.user)

    sorular = Sorular.objects.all()
    search = ''
    if request.method == 'POST':
        search = request.GET.get('search')
        # i burada harf duyarlılıgı , contains ise içinde benzeri var m ıkontrol
        sorular = Sorular.objects.filter(soru__icontains=search)
    context = {
        'kategoriler': kategoriler,
        'kullanicilar': kullanicilar,
        'son_kategori': son_kategori,
        'son_kullanıcı': son_kullanıcı,
        'sorular': sorular,
    }

    return render(request, "index.html", context)


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


@login_required(login_url='login')
def create_ask(request):
    kategoriler=Kategoriler.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        soru = request.POST['soru']
        isAnonim = request.POST.get('isAnonim', False)
        kategori_id=request.POST['kategori']

        kategori = Kategoriler.objects.get(id=kategori_id)
        if isAnonim == "on":
            isAnonim = True

        if isAnonim == True:
            username = "Anonymous User"
        #    print(username._len_())

        sorular = Sorular(username=username, soru=soru,
                          isAnonim=isAnonim, kullanici=request.user,category=kategori)
        sorular.save()
        return redirect('sorular')

    return render(request, 'soru-olustur.html', {"pageTitle": "Soru Sor","kategoriler":kategoriler})


@login_required(login_url='login')
def questionP(request):
    sor = Sorular.objects.all()
    cevap = Cevaplar.objects.all()
    kategoriler = Kategoriler.objects.all()

    arama = Sorular.objects.all()
    search = ''
    if request.method == 'POST':
        search = request.POST['search']
        arama = Sorular.objects.filter(soru__icontains=search)
    context = {
        'sorular': sor,
        'cevaplar': cevap,
        'kategoriler': kategoriler,
        'arama': arama
    }
    return render(request, 'sorular.html', context)

def getCategory(request,kategori):
    soru = Sorular.objects.filter(category__kategori=kategori)
    kategori = Kategoriler.objects.all()
    cevap = Cevaplar.objects.all()
    kategor=Kategoriler.objects.all()
    context = {
        'categories':kategori,
        'sorular':soru,
        'cevaplar':cevap,
        'kategoriler':kategor
    } 
    return render(request,'kategori_soru.html',context)


def arama(request):
    arama = Sorular.objects.all()
    cevap = Cevaplar.objects.all()
    kategoriler=Kategoriler.objects.all()
    search = ''
    if request.method == 'POST':
        search = request.POST.get('search')
        arama = Sorular.objects.filter(soru__icontains=search)
        print(arama)
    # else:
    #     arama = Sorular.objects.filter(soru__icontains=search)
    context = {
        'arama': arama,
        'cevaplar': cevap,
        'kategoriler':kategoriler
    }
    return render(request, 'search.html', context)


@login_required(login_url='login')
def create_answer(request):
    soru = Sorular.objects.last()
    if request.method == 'POST':
        # username = request.POST['username']
        cevap = request.POST['cevap']
        
        cevaplar = Cevaplar.objects.create(cevap=cevap,sorular=soru)
        cevaplar.save()

        return redirect('sorular')

    return render(request, 'create-answer.html')
