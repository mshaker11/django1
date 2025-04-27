from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Item

def home(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def createItem(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Item.objects.create(name=name)
        messages.success(request, "Item created successfully!")
        return redirect('/')
    return render(request, 'create_item.html')

def updateItem(request, pk):
    item = Item.objects.get(id=pk)

    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.save()
        messages.success(request, "Item updated successfully!")
        return redirect('/')
    return render(request, 'update_item.html', {'item': item})

def deleteItem(request, pk):
    item = Item.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        messages.success(request, "Item deleted successfully!")
        return redirect('/')
    return render(request, 'delete_item.html', {'item': item})

