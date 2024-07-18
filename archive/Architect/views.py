from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Building , Archive, ChefProject, Widgets
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
# Create your views here.
def home(request):
    images = Widgets.objects.all()
    return render(request, 'home.html', {'images': images})

def project(request):
    old_buildings = Building.objects.filter(state='ancien')
    new_buildings = Building.objects.filter(state='nouveau')
    context = {
        'old_buildings': old_buildings,
        'new_buildings': new_buildings,
    }
    return render(request, 'project.html', context)

def news(request):
    old_archives = Archive.objects.filter(state='ancien')
    new_archives = Archive.objects.filter(state='nouveau')
    archives = {
        'old_archives': old_archives,
        'new_archives': new_archives,
    }
    return render(request, 'news.html', archives)

def contact(request):
    chefs = ChefProject.objects.all()
    return render(request, 'contact.html', {'chefs': chefs})


def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("connexion")
    else:
        form =  CustomUserCreationForm()
    return render(request , 'inscription.html', {'form':form})


def connexion(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Nom de\'utilisateur ou mot de passe incorrect.")
    
    return render(request, 'connexion.html')
@login_required
def acceuil(request):
    return render(request, 'home.html')


def deconnexion(request):
    logout(request)
    return redirect('connexion')