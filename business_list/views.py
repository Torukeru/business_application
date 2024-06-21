from django.shortcuts import render, redirect
from .models import Stall,User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
# Create your views here.

def index_stall(request):
    stalls=Stall.objects.all()
    context = {
        'stalls': stalls
    }
    return render(request, 'stall/index.html', context)

def create_stall(request):
    return render(request, 'stall/create.html')

def store_stall(request):
    stallType = request.POST.get('stall_type')
    stallName = request.POST.get('stall_name')
    stallLocation = request.POST.get('stall_location')
    Stall.objects.create(stall_type=stallType, stall_name=stallName, stall_location=stallLocation)
    return redirect('/stall')

def show_stall(request,stall_id):
    stall = Stall.objects.get(pk=stall_id)
    
    context = {
        'stall': stall, 
    }
    return render(request, 'stall/show.html', context)
def edit_stall(request, stall_id):
    stall = Stall.objects.get(pk=stall_id)
    context={
        'stall': stall
    }
    return render(request, 'stall/edit.html', context)

def update_stall(request, stall_id):
    stallType = request.POST.get('stall_type')
    stallName = request.POST.get('stall_name')
    stallLocation = request.POST.get('stall_location')
    
    Stall.objects.filter(pk=stall_id).update(stall_type=stallType, stall_name=stallName, stall_location=stallLocation) # UPDATE genders SEt gender = gender WHERE gender_id = gender_id
    messages.success(request, 'Gender successfully updated')
    
    return redirect('/stall') # From urls.py

def delete_stall(request, stall_id):
    stall = Stall.objects.get(pk=stall_id)
    context = {
        'stall': stall
    }
    return render(request, 'stall/delete.html', context)

def destroy_stall(request, stall_id):
    Stall.objects.filter(pk=stall_id).delete()
    return redirect('/stall')


def index_user(request):
    users = User.objects.all() # SELECT * FROM users LEFT JOIN genders ON users.gender_id = gender.gender_id
    
    context = {
        'users': users, 
    }
    return render(request, 'user/index.html')


def create_user(request):
    users = User.objects.all()
    
    context = {
        'users': users
    }
    
    return render(request, 'user/create.html', context)

def store_user(request):
    firstName = request.POST.get('first_name')
    middleName = request.POST.get('middle_name')
    lastName = request.POST.get('last_name')
    age = request.POST.get('age')
    birthDate = request.POST.get('birth_date')
    gender = request.POST.get('gender')
    userName = request.POST.get('username')
    
        
    User.objects.create(first_name=firstName, middle_name=middleName, last_name=lastName, age=age, birth_date=birthDate, gender=gender, username=userName)
    messages.success(request, 'User successfully saved.')
