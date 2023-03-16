from django.shortcuts import render, redirect
from .models import Tarea, Tarea2
from .forms import TareaForm, Tarea2Form

# Create your views here.
def home(request):
    tareas = Tarea.objects.all()
    context = {'tareas': tareas, 'nbar': 'home'}
    return render(request, "todo/home.html", context)

def tareasnuevas(request):
    tareas = Tarea2.objects.all()
    context = {'tareas': tareas, 'nbar': 'tareasnuevas'}
    return render(request, "todo/tareasnuevas.html", context)

def agregar(request, model):
    if model == 'home':
        form = TareaForm()
    elif model == 'tareasnuevas': 
        form = Tarea2Form()

    if request.method == "POST":
        if model == 'home':
            form = TareaForm(request.POST)
        elif model == 'tareasnuevas': 
            form = Tarea2Form(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect(model)

    context = {'form': form}

    return render(request, "todo/agregar.html", context)

def eliminar(request, tarea_id, model):
    if model == 'home':
        tarea = Tarea.objects.get(id=tarea_id)
    elif model == 'tareasnuevas':
        tarea = Tarea2.objects.get(id=tarea_id)
    tarea.delete()
    return redirect(model)

def editar(request, tarea_id, model):
    if model == 'home':
        tarea = Tarea.objects.get(id=tarea_id)
        form = TareaForm(instance=tarea)
    elif model == 'tareasnuevas':
        tarea = Tarea2.objects.get(id=tarea_id)
        form = Tarea2Form(instance=tarea)

    if request.method =='POST':
        if model == 'home':
            form = TareaForm(request.POST, instance=tarea)
        if model == 'tareasnuevas':
            form = Tarea2Form(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect(model)

    context = {'form': form}
    
    return render(request, "todo/editar.html", context)