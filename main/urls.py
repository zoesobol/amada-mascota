from django.urls import path, include
from . import views

#magui
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='home'),
    path('acerca-de/', views.about, name='about'),

    path('suscripciones/<int:de_donde>/', login_required(views.suscripciones), name='suscripciones'),
    path('suscripciones_ver/<int:de_donde>/', login_required(views.suscripciones_ver), name='suscripciones_ver'),
    path('suscripciones_mod/<int:pk>/',login_required(views.SuscripcionActualizar.as_view()),name='suscripciones_mod'),    
    path('suscripciones_can/<int:pk>/',login_required(views.SuscripcionCancelar.as_view()),name='suscripciones_can'),    
]