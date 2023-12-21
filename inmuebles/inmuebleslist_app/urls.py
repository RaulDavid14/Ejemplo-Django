#esta clase maneja la clase path que sirve para interactuar con el navegador desde el sistema.
from django.urls import path

#hacemos referencia al archivo con el cual importamos la funcion que se dispara al momento de ingresa
from inmuebleslist_app.views import inmueble_list
from inmuebleslist_app.views import inmueble_detalle



urlpatterns = [
    path('list/', inmueble_list, name='inmueble_list'),
    path('<int:pk>', inmueble_detalle, name='inmueble_detalle')
]
