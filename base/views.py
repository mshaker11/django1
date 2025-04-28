from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .models import Item

def home(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

@login_required(login_url='login')
def createItem(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Item.objects.create(name=name)
        messages.success(request, "Item created successfully!")
        return redirect('/')
    return render(request, 'create_item.html')

@login_required(login_url='login')
def updateItem(request, pk):
    item = Item.objects.get(id=pk)

    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.save()
        messages.success(request, "Item updated successfully!")
        return redirect('/')
    return render(request, 'update_item.html', {'item': item})

@login_required(login_url='login')
def deleteItem(request, pk):
    item = Item.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        messages.success(request, "Item deleted successfully!")
        return redirect('/')
    return render(request, 'delete_item.html', {'item': item})

def logoutUser(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')
from django.contrib.auth import authenticate, login

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')
