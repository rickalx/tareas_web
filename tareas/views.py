from django.shortcuts import render, redirect
from django.contrib import messages

# import tareas form and models

from .forms import TareasForm
from .models import Tareas

# Create your views here.

def index(request):

    item_list = Tareas.objects.order_by("-fecha")
    if request.method == "POST":
        form = TareasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tareas')
    form = TareasForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "LISTA DE TAREAS",
    }
    return render(request, 'tareas/index.html', page)

### function to remove item, it receive tareas item_id as primary key from url ###
def remove(request, item_id):
    item = Tareas.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Item eliminado!")
    return redirect('tareas')

    