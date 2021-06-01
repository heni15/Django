from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop')
    else:
        form = ProduitForm()
        return render(request,'majProduits.html',{'form':form})
    
def shop(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('magasin')
    else:
        form = CommandeForm()
        return render(request,'cammande.html',{'form':form})
        
        
def vetrine(request):
    listp = Produit.objects.all()
    return render(request,'vitrine.html',{'list':listp})

def forni(request):
    listf = Fournisseur.objects.all()
    return render(request,'fornisseur.html',{'list':listf})

def forniprod(request, id):
    forni = Fournisseur.objects.get(id=id)
    forniprod = Produit.objects.filter(fournisseur=forni)
    return render(request,'forniprod.html',{'list':forniprod})

def viewshop(request):
    com = Commander.objects.all()
    return render(request,'viewshop.html',{'com':com})
def viewshopcard(request,id):
    com = Commander.objects.get(id=id)
    return render(request,'viewshopcard.html',{'com':com})