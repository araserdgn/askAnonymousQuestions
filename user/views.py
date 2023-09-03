from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

# !
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from user.forms import ProfileForm
from user.models import*


# Create your views here.
def userRegister(request):
    if request.method=='POST':
        kullanici = request.POST.get("kullanici", "default value")
        email = request.POST.get("email", "default value")
        sifre = request.POST.get("sifre", "default value")
        sifre2 = request.POST.get("sifre2", "default value")
        if sifre==sifre2:
            if User.objects.filter(username=kullanici).exists():
                messages.error(request , 'Kullanıcı adı zaten mevcuttur.')
            elif User.objects.filter(email = email).exists():
                messages.error(request,'Email zaten mevcuttur')
            elif len(sifre) < 6 :
                messages.error(request , 'Sifre en az 6 karakter olmalıdır')
            elif kullanici.lower() in sifre.lower() :
                messages.error(request , 'Kullanıcı adı ile sifre benzer olamaz')
            else:
                user = User.objects.create_user(
                    username=kullanici,
                    email = email,
                    password=sifre
                )  
                user.save()  
            
        user = authenticate(request, username=kullanici , password = sifre)
                
        if user is not None:
                login(request,user)
                messages.success(request,'Giriş Başarılı Şekilde Yapıldı.')
                new=Profile()
                new.owner=request.user
                new.nickname=kullanici
                new.email=email
                new.save()

                return render(request,'index.html')
        else:
            messages.error(request,'sifreler eşlesmedi')
    return render(request,'register.html')

def userLogin(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        sifre = request.POST['sifre']

        user = authenticate(request, username=kullanici , password = sifre)

        if user is not None:
            login(request,user)
            messages.success(request,'Giriş Başarılı Şekilde Yapıldı.')
            return redirect('index')
        else:
            messages.error(request,'Kullanıcı adı veya şifre Hatalıdır.!')    
            return redirect('login')
    return render (request,'login.html')  


def userLogout(request): 
    logout(request)       
    return redirect('index')

@login_required(login_url='login')
def profil_update(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            oldForm=Profile.objects.get(owner=request.user)
            newForm=form.save(commit=False)
            oldForm.nickname=newForm.nickname
            oldForm.isim=newForm.isim
            oldForm.resim=newForm.resim
            oldForm.email=newForm.email
            oldForm.save()
            return redirect('index')
    
    context = {
        'form':form
    }
    return render(request, 'profil_update.html',context)

        
@login_required(login_url='login')
def profil(request):
    profiller=Profile.objects.filter(owner=request.user)
    context = {
        'profiller': profiller,
    }
    return render(request, 'profil.html', context)
    # if request.method == 'POST':
    #     form = ProfileForm(request.POST,request.FILES)
    #     if form.is_valid():
    #         newProfile=form.save(commit=False)
            
    #         # newProfile.user =request.user
    #         # newProfile.save()
    #         try:
    #             old=Profile.objects.get(user=request.user)
    #             old.user=newProfile.user
    #             old.nickname=newProfile.nickname
    #             old.isim=newProfile.isim
    #             old.resim=newProfile.resim
    #             old.email=newProfile.email
    #             old.save()
    #         except:
    #             newP=ProfileForm(request.POST,request.FILES)
    #             newP.user=newProfile.user
    #             newP.nickname=newProfile.nickname
    #             newP.isim=newProfile.isim
    #             newP.resim=newProfile.resim
    #             newP.email=newProfile.email
    #             newP.save()
   
    #         messages.success(request, 'Profil Olustu')
    #         return render(request,"profil.html")


    # if request.method == 'POST':
    #     isim = request.POST['isim']
    #     nickname = request.POST['nickname']
    #     email = request.POST['email']
    #     konum = request.POST['konum']
    #     resim = request.FILES.get('resim')


    #     profilim = Profile(isim = isim , nickname = nickname , email = email, konum = konum, resim = resim)
    #     profilim.save()
    #     return redirect('index')
