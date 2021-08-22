from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    #AGREGO EL PATH PARA LA PAGINA DE URLS:
    path('holamundo/',include('HolaMundo.urls'))
]
