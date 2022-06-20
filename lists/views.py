
from django.http import HttpResponse
from django.shortcuts import render
from lists.models import Item
from django.shortcuts import redirect

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items':items})

def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return