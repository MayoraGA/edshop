from django.urls import path, include
from . import views

# Codigo para saber donde esta cada url los enlaces de la aplicacion
app_name = "web"

urlpatterns = [
    path('', views.index, name="index"),
    path('productosPorCategoria/<int:categoria_id>/',
         views.productosPorCategoria, name='productosPorCategoria'),
    path('productosPorNombre/', views.productosPorNombre, name="productosPorNombre"),
    path('producto/<int:producto_id>/', views.productoDetalle, name="producto"),


]
