# Generated by Django 4.0 on 2022-07-22 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('Z2', 'Zidor 2'), ('Z3', 'Zidor 3'), ('KOS', 'Koskorrak'), ('KAS1', 'Kaskondoak 1')], default='Z2', max_length=100)),
                ('er', models.ForeignKey(default='Kaskondoak', on_delete=django.db.models.deletion.CASCADE, to='documentation.er')),
            ],
        ),
        migrations.CreateModel(
            name='Trimestre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(choices=[(1, 'Primero'), (2, 'Segundo'), (3, 'Tercero')], default=1)),
                ('texto', models.TextField()),
                ('grupo', models.ForeignKey(default='Kaskondoak 1', on_delete=django.db.models.deletion.CASCADE, to='documentation.grupo')),
            ],
        ),
        migrations.CreateModel(
            name='Taller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('foto', models.ImageField(upload_to='')),
                ('grupo', models.ForeignKey(default='Kaskondoak 1', on_delete=django.db.models.deletion.CASCADE, to='documentation.grupo')),
            ],
        ),
        migrations.CreateModel(
            name='Simbolo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to='')),
                ('grupo', models.ForeignKey(default='Kaskondoak 1', on_delete=django.db.models.deletion.CASCADE, to='documentation.grupo')),
            ],
        ),
        migrations.CreateModel(
            name='Reunion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('texto', models.TextField()),
                ('trimestre', models.ForeignKey(default='Primero', on_delete=django.db.models.deletion.CASCADE, to='documentation.trimestre')),
            ],
        ),
        migrations.CreateModel(
            name='Paso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('grupo', models.ForeignKey(default='Kaskondoak 1', on_delete=django.db.models.deletion.CASCADE, to='documentation.grupo')),
            ],
        ),
        migrations.CreateModel(
            name='Monte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('foto', models.ImageField(upload_to='')),
                ('trimestre', models.ForeignKey(default='Primero', on_delete=django.db.models.deletion.CASCADE, to='documentation.trimestre')),
            ],
        ),
        migrations.CreateModel(
            name='Campamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('PA', 'Paso'), ('NA', 'Navidad'), ('SS', 'Semana Santa'), ('VE', 'Verano')], default='NA', max_length=2)),
                ('trimestre', models.ForeignKey(default='Primero', on_delete=django.db.models.deletion.CASCADE, to='documentation.trimestre')),
            ],
        ),
    ]