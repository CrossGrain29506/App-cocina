# Generated by Django 4.1.7 on 2023-02-24 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cat_img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='imagenes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('URL', models.ImageField(upload_to='pics/%y/%m/%d/')),
                ('cat_img', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Coque.cat_img')),
            ],
        ),
        migrations.CreateModel(
            name='paises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('cat_img', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Coque.cat_img')),
                ('img_bandera', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Coque.imagenes')),
            ],
        ),
        migrations.CreateModel(
            name='recetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('sinopsis', models.TextField()),
                ('ingredientes', models.TextField()),
                ('proceso', models.TextField()),
                ('like', models.IntegerField()),
                ('cat_img', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Coque.cat_img')),
                ('img', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Coque.imagenes')),
                ('pais', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Coque.paises')),
            ],
        ),
    ]