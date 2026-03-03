"""
URL configuration for App_Gestion_Escolar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.base , name="base"),
    path('admin/', admin.site.urls, name="admin"),
    path('alumnos/', include('alumnos.urls')),
    path('cursos/', include('cursos.urls')),
    path('profesores/', include('profesores.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('sobre_nosotros/', views.sobre_nosotros, name="sobre_nosotros"),
    path('contacto/', views.contacto, name="contacto"),
    path('ayuda/', views.ayuda, name="ayuda"),
    path('Term_acc_priva/', views.term_acc_priva, name="Term_acc_priva"),
    path('reglamento/', views.reglamento, name="reglamento"),
    path('directorio_docente/', views.directorio_docente, name="directorio_docente"),


]



# Configuración de media para desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configuración de errores
handler404 = 'App_Gestion_Escolar.views.error_404'
handler500 = 'App_Gestion_Escolar.views.error_500'