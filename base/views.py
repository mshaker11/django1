from django.shortcuts import render, redirect
from .models import Item

def home(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def createItem(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Item.objects.create(name=name)
        return redirect('/')
    return render(request, 'create_item.html')
def updateItem(request, pk):
    item = Item.objects.get(id=pk)

    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.save()
        return redirect('/')

    return render(request, 'update_item.html', {'item': item})
def deleteItem(request, pk):
    item = Item.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    return render(request, 'delete_item.html', {'item': item})
