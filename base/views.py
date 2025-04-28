from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .models import Item, Room, Activity, Message
from django.contrib.auth.models import User

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

from django.contrib.auth.forms import UserCreationForm

def registerUser(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)

def roomList(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'room_list.html', context)

@login_required(login_url='login')
def createRoom(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        room = Room.objects.create(
            host=request.user,
            name=name,
            description=description
        )

        # Log activity for room creation
        Activity.objects.create(user=request.user, action=f"Created room: {name}")

        messages.success(request, "Room created successfully!")
        return redirect('room-list')
    return render(request, 'create_room.html')

@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == 'POST':
        room.name = request.POST.get('name')
        room.description = request.POST.get('description')
        room.save()

        # Log activity for room update
        Activity.objects.create(user=request.user, action=f"Updated room: {room.name}")

        messages.success(request, "Room updated successfully!")
        return redirect('room-list')

    context = {'room': room}
    return render(request, 'update_room.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == 'POST':
        room.delete()

        
        Activity.objects.create(user=request.user, action=f"Deleted room: {room.name}")

        messages.success(request, "Room deleted successfully!")
        return redirect('room-list')

    context = {'room': room}
    return render(request, 'delete_room.html', context)
def activityFeed(request):
    # Fetch all Activity records, newest first
    activities = Activity.objects.all().order_by('-timestamp')
    return render(request, 'activity_feed.html', {
        'activities': activities
    })

def profileUser(request, pk):
    user_obj = User.objects.get(id=pk)
    
    rooms = Room.objects.filter(host=user_obj)
    
    messages_posted = Message.objects.filter(user=user_obj).order_by('-created_at')
    context = {
        'profile_user': user_obj,
        'rooms': rooms,
        'messages_posted': messages_posted
    }
    return render(request, 'profile.html', context)
from django.contrib.auth.forms import UserChangeForm

@login_required(login_url='login')
def editAccount(request):
    user = request.user
    form = UserChangeForm(instance=user)

    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Account updated successfully!")
            return redirect('profile', pk=user.id)

    context = {'form': form}
    return render(request, 'edit_account.html', context)
