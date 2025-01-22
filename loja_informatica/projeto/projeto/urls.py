from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loja_informatica.urls')),  # Define que '/' redireciona para loja_informatica
    path('loja/', include('loja_informatica.urls')),  # Caminho adicional para /loja/
]