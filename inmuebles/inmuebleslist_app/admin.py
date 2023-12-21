from django.contrib import admin
#mandamos llamar el  archivo del modelo
from inmuebleslist_app.models import Inmueble


# Register your models here.
#definimos los modelos que se van a utilizar dentro del entorno de django para su manejo. 
admin.site.register(Inmueble)