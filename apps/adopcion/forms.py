from django import forms
from apps.perdidos.models import Ubicacion,Mascota,Adopcion
from apps.perdidos.models import Publicacion, Encontro, lista_especies, lista_localidades

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields =  '__all__'
        widgets = {
         'localidad': forms.Select(attrs= {'class': 'form-control'}),
         'barrio': forms.TextInput(attrs= {'class': 'form-control'}),
         'entre_calles': forms.TextInput(attrs= {'class': 'form-control'}),
         'numero': forms.TextInput(attrs= {'class': 'form-control'}),
         'calle': forms.TextInput(attrs= {'class': 'form-control'}),
         'otros_datos': forms.Textarea(attrs= {'class': 'form-control', 'rows': 2, 'style': 'resize: none;'}),
        }
        

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fileds = '__all__'
        exclude = ['id_dueño']
        widgets = {
         'id_dueño': forms.Select(attrs= {'name': 'id_dueño', 'hidden': '',}),
         'nombre': forms.TextInput(attrs= {'class': 'form-control'}),
         'familia': forms.TextInput(attrs= {'class': 'form-control'}),
         'raza': forms.TextInput(attrs= {'class': 'form-control'}),
         'especie': forms.Select(attrs= {'class': 'form-control'}),
         'sexo': forms.Select(attrs= {'class': 'form-control'}),
         'color': forms.TextInput(attrs= {'class': 'form-control'}),
         'otro_dato': forms.Textarea(attrs= {'class': 'form-control', 'rows': 3, 'style': 'resize: none;'}),
         'edad': forms.TextInput(attrs= {'class': 'form-control'}),
         'tamaño': forms.Select(attrs= {'class': 'form-control'}),
         'fotos': forms.FileInput(attrs= {'class': 'form-control'}),
        }
        labels = {
            'id_dueño': '',
            'nombre': 'Mascota',
            'otro_dato': 'Alguna descripción adicional',
            'edad': 'Edad aproximada',
        }

class AdopcionForm(forms.ModelForm):
    class Meta:
        model = Adopcion
        fields = '__all__'
        exclude =  ['id_usuario','id_mascota','id_ubicacion','fecha_publicacion']
        widgets = {
            'condicion':forms.Textarea(attrs= {'class': 'form-control', 'rows': 3, 'style': 'resize: none;'}),
        }


class SearchForm(forms.Form):
   barrio = forms.CharField(max_length=30, required = False)
   ORDER_OPCIONES = (
      ("sin", "Sin Orden"),
      ("Fecha",(
         ("antiguo", "Publicaciones antiguas"),
         ("nuevo", "Publicaciones recientes"))
      ))
   n  = ("sin","Sin eleccion")
   l = list(lista_especies)
   l.append(n) 
   l_especies = tuple(l)

   l = list(lista_localidades)
   l.append(n) 
   l_localidades = tuple(l)

   orden = forms.ChoiceField(choices=ORDER_OPCIONES, required = False, initial="nuevo")
   especie = forms.ChoiceField(choices=l_especies, required = False, initial = "sin")
   localidad = forms.ChoiceField(choices=l_localidades, required = False, initial="sin")
   #barrio = forms.ModelChoiceField(queryset=Ubicacion.objects.all(), widget=forms.SelectMultiple, required = False)
   #permitir_comentarios = forms.BooleanField(required = False)
    
   def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields["barrio"].widget.attrs["placeholder"] = "Barrio"
        #self.fields["permitir_comentarios"].widget.attrs["class"] ="with-gap"