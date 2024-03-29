from django.shortcuts import render, redirect, get_object_or_404
from apps.perdidos.models import Publicacion, Mascota, Ubicacion, Perdido
from .forms import MascotaForm, UbicacionForm, PerdidoForm, SearchForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import datetime, timedelta

# Create your views here.

@login_required
def lista_perdidos(request):
   current_user = request.user
   publicaciones = Perdido.objects.filter(id_usuario=current_user)
   ctx = {
      'publicaciones': publicaciones,
      'fecha_actual': datetime.now().date(),
   }
   return render(request, 'lista_perdidos.html', ctx)

@login_required
def publicar(request):
   current_user = request.user
   mascota = MascotaForm(initial= {'id_dueño': current_user})
   ubicacion = UbicacionForm()
   perdido = PerdidoForm(initial= {'id_usuario': current_user})
   if request.method == 'POST':
      mascota = MascotaForm(data=request.POST, files=request.FILES)
      ubicacion = UbicacionForm(data=request.POST)
      perdido = PerdidoForm(data=request.POST, initial={'id_usuario': current_user})
      if mascota.is_valid() and ubicacion.is_valid() and perdido.is_valid():
         masc = mascota.save()
         ubic = ubicacion.save()
         enc = perdido.save(commit=False)
         enc.id_usuario = current_user
         enc.id_mascota = masc
         enc.id_ubicacion = ubic
         enc.save()
        
         messages.success(request, f'Su publicación ha sido un exito!! Recuerda renovarla antes de 7 días.')
         return redirect(to='perdidos:lista_perdidos')
      else:
         messages.error(request, 'Ups...parece que algo salió mal.!! Vuelve a intentarlo.')
         mascota = MascotaForm(data=request.POST, files=request.FILES)
         ubicacion = UbicacionForm(data=request.POST)
         perdido = PerdidoForm(data=request.POST)
   
   ctx = {
      'mascota': mascota,
      'ubicacion': ubicacion,
      'perdido': perdido,
      }
   return render(request, 'publicar_p.html', ctx)

@login_required
def editar_publicacion(request, id_publicacion):
   current_user = request.user
   perdido = get_object_or_404(Perdido, id=id_publicacion, id_usuario=current_user)
   mascota = get_object_or_404(Mascota, id=perdido.id_mascota.id)
   ubicacion = get_object_or_404(Ubicacion, id=perdido.id_ubicacion.id)
   if request.method == 'POST':
      mascota = MascotaForm(data=request.POST, files=request.POST, instance=mascota)
      ubicacion = UbicacionForm(data=request.POST, instance=ubicacion)
      perdido = PerdidoForm(data=request.POST, instance=perdido)
      if mascota.is_valid() and ubicacion.is_valid() and perdido.is_valid():
         mascota.save()
         ubicacion.save()
         perdido.save()
         messages.success(request, 'Guardado')
         return redirect(to='perdidos:lista_perdidos')
      else:
         messages.error(request, 'Ups...parece que algo salió mal.!! Vuelve a intentarlo.')
   ctx = {
      'mascota': MascotaForm(instance=mascota),
      'ubicacion': UbicacionForm(instance=ubicacion),
      'perdido': PerdidoForm(instance=perdido),
   }
   return render(request, 'editar_publicacion_p.html', ctx)

# @login_required
def publicacion(request, id_publicacion):
   #current_user = request.user
   publicacion = get_object_or_404(Perdido, id=id_publicacion) #, id_usuario=current_user)
   ctx = {
      'publicacion': publicacion,
      'fecha_actual': datetime.now().date(),
   }
   return render(request, 'publicacion_p.html', ctx)

@login_required
def eliminar_publicacion(request, id_publicacion):
   current_user = request.user
   publicacion = get_object_or_404(Perdido, id=id_publicacion, id_usuario=current_user)
   mascota = Mascota.objects.get(id=publicacion.id_mascota.id)
   ubicacion = Ubicacion.objects.get(id=publicacion.id_ubicacion.id)
   publicacion.delete()
   mascota.delete()
   ubicacion.delete()
   return redirect(to='perdidos:lista_perdidos')


def buscar_p(request):
   if request.GET:
      search_form = SearchForm(request.GET)
   else:
      search_form = SearchForm()

   barrio = request.GET.get("barrio", "") ## recibe barrio
   especie = request.GET.get("especie","")
   orden_post = request.GET.get("orden", None)
   localidad = request.GET.get("localidad","")
   #param_comentarios_habilitados = request.GET.get("permitir_comentarios", None)
   #param_categorias = request.GET.getlist("barrio")

   publicaciones=Perdido.objects.all().filter(id_ubicacion__barrio__icontains = barrio, valido_hasta__gt = timezone.now()).order_by("-fecha_evento")
   publicaciones.exclude(fecha_entrega__isnull=False)
   if especie and especie != "sin":
      publicaciones = publicaciones.filter(id_mascota__especie__icontains = especie)
  
   if localidad and localidad !="sin":
      publicaciones = publicaciones.filter(id_ubicacion__localidad__icontains = localidad)
   #posts = Ubicacion.objects.filter(barrio__icontains = filtro_barrio).values_list('barrio')
   
   if orden_post == "sin":
      publicaciones = publicaciones.order_by()
   elif orden_post == "antiguo":
      publicaciones = publicaciones.order_by("fecha_evento")
   elif orden_post == "nuevo":
      print('pasa nuevo')
      publicaciones = publicaciones.order_by("-fecha_evento")

   #print(publicaciones)
   contexto = {"publicaciones":publicaciones,
              "search_form":search_form,
               }
   return render(request, "index_perdidos.html",contexto)
   
@login_required
def renovar_publicacion(request, id_publicacion):
   current_user = request.user
   fecha_actual = datetime.now().date()
   publicacion = get_object_or_404(Perdido, id=id_publicacion, id_usuario=current_user)
   # print(fecha_actual)
   # print(publicacion.valido_hasta)
   if fecha_actual > publicacion.valido_hasta:
      publicacion.valido_hasta = fecha_actual + timedelta(days=7)
      publicacion.save()
      # print('SI')
   return redirect(to='perdidos:lista_perdidos')
