# Generated by Django 4.2.1 on 2023-05-08 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Carrera')),
                ('duracion', models.IntegerField(choices=[(1, 'UNO'), (2, 'DOS'), (3, 'TRES')], verbose_name='Duracion')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Creado el')),
                ('update_at', models.DateTimeField(auto_now_add=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'Carrera',
                'verbose_name_plural': 'Carreras',
            },
        ),
    ]