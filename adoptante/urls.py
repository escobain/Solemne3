from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.index,name="index" ),
    path('registro/',views.registro, name="registro"),
    path('registro/crear', views.crear,name="crear"),
    path('registro/buscar/<str:var>',views.buscar, name="buscar"),
    path('registro/eliminar/<str:var>',views.eliminar,name="eliminar"),
    path('registro/editar/<str:var>', views.editar,name="editar"),
    path('registro/edicion/<str:var>', views.edicion,name="edicion")
]
