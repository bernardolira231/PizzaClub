from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='Home'),
    path('agregar/<int:producto_id>', views.agregarProducto, name='Add'),
    path('eliminar/<int:producto_id>', views.eliminarProducto, name='Del'),
    path('restar/<int:producto_id>', views.restarProducto, name='Sub'),
    path('limpiar/', views.limpiarCarrito, name='cls'),
    path('carrito/', views.carrito, name='Carrito'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
