from Appventas import views
from django.urls import path


urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('about', views.about, name='about'),

    path('clientes/', views.clienteslistview.as_view(), name='listaclientes'),
    path('clientes/nuevo', views.clientescreateview.as_view(), name='nuevocliente'),
    path('clientes/<pk>', views.clientesdetalle.as_view(), name='clientesdetalle'),
    path('clientes/<pk>/editar', views.clientesupdateview.as_view(), name='clienteseditar'),
    path('clientes/<pk>/borrar', views.clientesdeleteview.as_view(), name="clientesborrar"),

    path('productos/', views.productoslistview.as_view(), name='listaproductos'),
    path('productos/nuevo', views.productoscreateview.as_view(), name='nuevoproducto'),
    path('productos/<pk>', views.productosdetalle.as_view(), name='productosdetalle'),
    path('productos/<pk>/editar', views.productosupdateview.as_view(), name='productoseditar'),
    path('productos/<pk>/borrar', views.productosdeleteview.as_view(), name="productosborrar"),
    
    path('servicios/', views.servicioslistview.as_view(), name='listaservicios'),
    path('servicios/nuevo', views.servicioscreateview.as_view(), name='nuevoservicio'),
    path('servicios/<pk>', views.serviciosdetalle.as_view(), name='serviciosdetalle'),
    path('servicios/<pk>/editar', views.serviciosupdateview.as_view(), name='servicioseditar'),
    path('servicios/<pk>/borrar', views.serviciosdeleteview.as_view(), name="serviciosborrar"),

    # path('busquedaproductos/', views.busquedaproductos, name='busquedaproductos'),
    # path('buscar/', views.buscar, name='buscar'),
]