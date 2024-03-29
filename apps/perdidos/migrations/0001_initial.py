# Generated by Django 3.1.6 on 2021-03-19 17:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Desconocido', help_text='Indica su nombre si lo conoces', max_length=30)),
                ('familia', models.CharField(default='Desconocido', max_length=50)),
                ('especie', models.CharField(choices=[('Cerdo', 'Cerdo'), ('Conejo', 'Conejo'), ('Erizo de tierra', 'Erizo de tierra'), ('Gallo', 'Gallo'), ('Gato', 'Gato'), ('Hámster', 'Hámster'), ('Loro', 'Loro'), ('Pato', 'Pato'), ('Perro', 'Perro'), ('Tortuga de tierra', 'Tortuga de tierra'), ('Vaca', 'Vaca')], help_text='Indica la especie', max_length=17)),
                ('raza', models.CharField(default='Desconocido', max_length=50)),
                ('tamaño', models.CharField(choices=[('Enorme', 'Enorme'), ('Grande', 'Grande'), ('Mediano', 'Mediano'), ('Chico', 'Chico'), ('Diminuto', 'Diminuto')], max_length=8)),
                ('edad', models.CharField(default='N', max_length=2)),
                ('sexo', models.CharField(choices=[('Macho', 'Macho'), ('Hembra', 'Hembra'), ('Desconocido', 'Desconocido')], max_length=11)),
                ('color', models.CharField(blank=True, max_length=30, null=True)),
                ('fotos', models.ImageField(upload_to='mascota')),
                ('otro_dato', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('id_dueño', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Adopcion', 'Adopcion'), ('Encontro', 'Encontro'), ('Perdido', 'Perdio')], max_length=8)),
                ('especie', models.CharField(choices=[('Cerdo', 'Cerdo'), ('Conejo', 'Conejo'), ('Erizo de tierra', 'Erizo de tierra'), ('Gallo', 'Gallo'), ('Gato', 'Gato'), ('Hámster', 'Hámster'), ('Loro', 'Loro'), ('Pato', 'Pato'), ('Perro', 'Perro'), ('Tortuga de tierra', 'Tortuga de tierra'), ('Vaca', 'Vaca')], max_length=20)),
                ('localidad', models.CharField(choices=[('Avia Terai', 'Avia Terai'), ('Campo Largo', 'Campo Largo'), ('Charata', 'Charata'), ('Colonia Benítez', 'Colonia Benítez'), ('Colonia Elisa', 'Colonia Elisa'), ('Colonias Unida', 'Colonias Unidas'), ('Comandancia Frías', 'Comandancia Frías'), ('Concepción del Bermejo', 'Concepción del Bermejo'), ('Coronel Du Graty', 'Coronel Du Graty'), ('Corzuela', 'Corzuela'), ('El Paranacito', 'El Paranacito'), ('El Sauzalito', 'El Sauzalito'), ('Fortín Belgrano', 'Fortín Belgrano'), ('Gancedo', 'Gancedo'), ('General José de San Martín', 'General José de San Martín'), ('General Pinedo', 'General Pinedo'), ('Hermoso Campo', 'Hermoso Campo'), ('Isla Soto', 'Isla Soto'), ('Juan José Castelli', 'Juan José Castelli'), ('La Clotilde', 'La Clotilde'), ('La Escondida', 'La Escondida'), ('La Leonesa', 'La Leonesa'), ('La Tigra', 'La Tigra'), ('La Verde', 'La Verde'), ('Las Breñas', 'Las Breñas'), ('Las Garcitas', 'Las Garcitas'), ('Las Hacheras', 'Las Hacheras'), ('Las Palmas', 'Las Palmas'), ('Los Frentones', 'Los Frentones'), ('Machagai', 'Machagai'), ('Makallé', 'Makallé'), ('Margarita Belén', 'Margarita Belén'), ('Miraflores', 'Miraflores'), ('Misión Nueva Pompeya', 'Misión Nueva Pompeya'), ('Napenay', 'Napenay'), ('Pampa del Indio', 'Pampa del Indio'), ('Pampa del Infierno', 'Pampa del Infierno'), ('Presidencia de la Plaza', 'Presidencia de la Plaza'), ('Presidencia Roca', 'Presidencia Roca'), ('Presidencia Roque Sáenz Peña', 'Presidencia Roque Sáenz Peña'), ('Puerto Bermejo', 'Puerto Bermejo'), ('Puerto Las Palmas', 'Puerto Las Palmas'), ('Puerto Tirol', 'Puerto Tirol'), ('Quitilipi', 'Quitilipi'), ('San Bernardo', 'San Bernardo'), ('Paraje San Fernando', 'Paraje San Fernando'), ('Santa Sylvina', 'Santa Sylvina'), ('Taco Pozo', 'Taco Pozo'), ('Tres Isletas', 'Tres Isletas'), ('Villa Ángela', 'Villa Ángela'), ('Villa Berthet', 'Villa Berthet'), ('Villa Río Bermejito', 'Villa Río Bermejito')], max_length=30)),
                ('fecha_desde', models.DateField(default=django.utils.timezone.now)),
                ('fecha_hasta', models.DateField()),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observaciones', models.CharField(default='Sin observaciones', max_length=100)),
                ('fecha_publicacion', models.DateField(auto_now_add=True)),
                ('fecha_evento', models.DateField(default=django.utils.timezone.now)),
                ('valido_hasta', models.DateField(default=datetime.datetime(2021, 3, 26, 17, 10, 44, 608456, tzinfo=utc))),
                ('fecha_entrega', models.DateField(blank=True, null=True)),
                ('id_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perdidos.mascota')),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localidad', models.CharField(choices=[('Avia Terai', 'Avia Terai'), ('Campo Largo', 'Campo Largo'), ('Charata', 'Charata'), ('Colonia Benítez', 'Colonia Benítez'), ('Colonia Elisa', 'Colonia Elisa'), ('Colonias Unida', 'Colonias Unidas'), ('Comandancia Frías', 'Comandancia Frías'), ('Concepción del Bermejo', 'Concepción del Bermejo'), ('Coronel Du Graty', 'Coronel Du Graty'), ('Corzuela', 'Corzuela'), ('El Paranacito', 'El Paranacito'), ('El Sauzalito', 'El Sauzalito'), ('Fortín Belgrano', 'Fortín Belgrano'), ('Gancedo', 'Gancedo'), ('General José de San Martín', 'General José de San Martín'), ('General Pinedo', 'General Pinedo'), ('Hermoso Campo', 'Hermoso Campo'), ('Isla Soto', 'Isla Soto'), ('Juan José Castelli', 'Juan José Castelli'), ('La Clotilde', 'La Clotilde'), ('La Escondida', 'La Escondida'), ('La Leonesa', 'La Leonesa'), ('La Tigra', 'La Tigra'), ('La Verde', 'La Verde'), ('Las Breñas', 'Las Breñas'), ('Las Garcitas', 'Las Garcitas'), ('Las Hacheras', 'Las Hacheras'), ('Las Palmas', 'Las Palmas'), ('Los Frentones', 'Los Frentones'), ('Machagai', 'Machagai'), ('Makallé', 'Makallé'), ('Margarita Belén', 'Margarita Belén'), ('Miraflores', 'Miraflores'), ('Misión Nueva Pompeya', 'Misión Nueva Pompeya'), ('Napenay', 'Napenay'), ('Pampa del Indio', 'Pampa del Indio'), ('Pampa del Infierno', 'Pampa del Infierno'), ('Presidencia de la Plaza', 'Presidencia de la Plaza'), ('Presidencia Roca', 'Presidencia Roca'), ('Presidencia Roque Sáenz Peña', 'Presidencia Roque Sáenz Peña'), ('Puerto Bermejo', 'Puerto Bermejo'), ('Puerto Las Palmas', 'Puerto Las Palmas'), ('Puerto Tirol', 'Puerto Tirol'), ('Quitilipi', 'Quitilipi'), ('San Bernardo', 'San Bernardo'), ('Paraje San Fernando', 'Paraje San Fernando'), ('Santa Sylvina', 'Santa Sylvina'), ('Taco Pozo', 'Taco Pozo'), ('Tres Isletas', 'Tres Isletas'), ('Villa Ángela', 'Villa Ángela'), ('Villa Berthet', 'Villa Berthet'), ('Villa Río Bermejito', 'Villa Río Bermejito')], max_length=30)),
                ('barrio', models.CharField(max_length=50)),
                ('calle', models.CharField(max_length=50)),
                ('numero', models.CharField(default='S/N', max_length=5)),
                ('entre_calles', models.CharField(blank=True, max_length=50, null=True)),
                ('otros_datos', models.CharField(default='Sin particular', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Adopcion',
            fields=[
                ('publicacion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='perdidos.publicacion')),
                ('condicion', models.CharField(default='Cuidar este hermoso ser vivo', max_length=300)),
            ],
            bases=('perdidos.publicacion',),
        ),
        migrations.CreateModel(
            name='Encontro',
            fields=[
                ('publicacion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='perdidos.publicacion')),
                ('cuida', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], help_text='Si tiene el animal y lo cuida indique Si, caso contrario No', max_length=2)),
                ('fecha_limite', models.DateField(blank=True, default=None, null=True)),
            ],
            bases=('perdidos.publicacion',),
        ),
        migrations.CreateModel(
            name='Perdido',
            fields=[
                ('publicacion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='perdidos.publicacion')),
                ('gratificacion', models.CharField(default='S/G', max_length=5)),
            ],
            bases=('perdidos.publicacion',),
        ),
        migrations.CreateModel(
            name='tiene_notificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leido', models.BooleanField(default=False)),
                ('id_notificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perdidos.notificacion')),
                ('id_publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perdidos.publicacion')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='publicacion',
            name='id_ubicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='perdidos.ubicacion'),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
