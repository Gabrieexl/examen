from django.urls import path
from . import views
app_name = 'gestionTienda'

urlpatterns =[
    path('', views.index, name='index'),
    path('registroTienda',views.registroTienda,name='registroTienda'),
    path('eliminarTienda/<str:idTienda>', views.eliminarTienda, name='eliminarTienda'),
    path('Productos',views.Productos,name='Productos'),
    path('eliminarProductos/<str:idProducto>', views.eliminarProducto, name='eliminarProductos'),
    path('asignarProducto',views.asignarProducto,name='asignarProducto'),
    path('verProductosTienda/<int:idTienda>/', views.verProductosTienda, name='verProductosTienda')
]
