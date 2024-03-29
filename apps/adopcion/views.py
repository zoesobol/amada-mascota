from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from . import models
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect,HttpResponse
from datetime import datetime, timedelta
from django.utils import timezone
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from apps.encontrados.forms import SearchForm

def index(request):
    context = {}
    return render(request,'index.html',context)    

class misAdopciones(ListView):
    model = Adopcion
    template_name = 'historial_adopciones.html'
    
    def get_queryset(self):
        return super().get_queryset().filter(id_usuario=self.request.user)

class AdopcionCrear(CreateView):
    model = Adopcion
    template_name = 'crear_adopcion.html'
    form_class = AdopcionForm
    ubicacion_form_class = UbicacionForm
    mascota_form_class = MascotaForm
    success_url = reverse_lazy('adopcion:adopciones_listar')

    def get_context_data(self,**kwargs):
        context = super(AdopcionCrear,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.ubicacion_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.mascota_form_class(self.request.GET)
        return context

    def post(self,request,*args,**kwargs):
        current_user = request.user
        self.object = self.get_object
        form = self.form_class(request.POST,initial={'id_usuario': current_user})
        form2 = self.ubicacion_form_class(request.POST)
        form3 = self.mascota_form_class(request.POST, request.FILES,initial={'id_usuario_id': current_user})
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            masc = form3.save(commit=False)
            masc.id_dueño = current_user
            masc.save()
            adopcion = form.save(commit=False)
            adopcion.id_usuario = current_user
            adopcion.id_ubicacion = form2.save()
            adopcion.id_mascota = masc
            adopcion.save()
            form3.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form = form,form2=form2,form3=form3))

@login_required
def renovar_publicacion(request, id):
    current_user = request.user
    fecha_actual = datetime.now().date()
    publicacion = get_object_or_404(Adopcion, id=id, id_usuario=current_user)
    if fecha_actual > publicacion.valido_hasta:
        publicacion.valido_hasta = fecha_actual + timedelta(days=7)
        publicacion.save()
    return redirect(to='adopcion:adopciones_listar')

class AdopcionActualizar(UpdateView):
    model = Adopcion
    form_class = AdopcionForm
    ubicacion_form_class = UbicacionForm
    mascota_form_class = MascotaForm
    template_name = 'crear_adopcion.html'
    success_url = reverse_lazy('adopcion:adopciones_listar')
    
    def get_context_data(self,**kwargs):
        context = super(AdopcionActualizar,self).get_context_data(**kwargs)
        if 'form2' not in context:
            context['form2'] = self.ubicacion_form_class(instance = self.object.id_ubicacion)
        if 'form3' not in context:
            context['form3'] = self.mascota_form_class(instance = self.object.id_mascota)
        return context

    def post(self,request,*args,**kwargs):
        current_user = request.user
        self.object = self.get_object
        form = self.form_class(request.POST,initial={'id_usuario': current_user},instance = self.get_object())
        form2 = self.ubicacion_form_class(request.POST,instance = self.get_object().id_ubicacion)
        form3 = self.mascota_form_class(request.POST,request.FILES,initial={'id_usuario_id': current_user},instance = self.get_object().id_mascota)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            adopcion = form.save(commit=False)
            adopcion.id_usuario = current_user
            adopcion.id_ubicacion = form2.save()
            adopcion.id_mascota = form3.save()
            adopcion.save()
            form3.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form = form,form2=form2,form3=form3))

class AdopcionEliminar(DeleteView):
    model = Adopcion
    form_class = AdopcionForm
    template_name = 'adopcion_eliminar.html'
    success_url = reverse_lazy('adopcion:adopciones_listar')

#@login_required
def verAdopcion(request, id):
   #current_user = request.user.pk
   adopcion = get_object_or_404(Adopcion, id=id,)# id_usuario=current_user)
   ctx = {
      'adopcion': adopcion,
   }
   return render(request, 'info_adopcion.html', ctx)
    

def buscar_a(request):
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

   publicaciones=Adopcion.objects.all().filter(id_ubicacion__barrio__icontains = barrio, valido_hasta__gt = timezone.now()).order_by("-fecha_evento")
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
   return render(request, "index_adopcion.html",contexto)
