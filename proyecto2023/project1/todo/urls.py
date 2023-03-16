from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tareasnuevas/", views.tareasnuevas, name="tareasnuevas"),
    path("agregar/<str:model>", views.agregar, name="agregar"),
    path("eliminar/<int:tarea_id>/<str:model>", views.eliminar, name="eliminar"),
    path("editar/<int:tarea_id>/<str:model>", views.editar, name="editar")
]