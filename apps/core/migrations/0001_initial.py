# Generated by Django 3.1.7 on 2021-10-09 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sitio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='Sitios')),
                ('ubicacion', models.TextField()),
                ('categoria', models.ManyToManyField(to='core.Categoria')),
            ],
        ),
    ]