# Generated by Django 5.1 on 2024-11-29 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(max_length=100, unique=True, verbose_name='nombre clave')),
                ('name', models.CharField(max_length=200, verbose_name='Red Social')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Enlace')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'enlace',
                'verbose_name_plural': 'enlaces',
                'ordering': ['-created'],
            },
        ),
    ]
