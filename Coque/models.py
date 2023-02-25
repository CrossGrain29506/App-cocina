from django.db import models

# Create your models here.
class cat_img(models.Model):
    nombre = models.CharField(max_length=200)
    url = models.URLField(max_length=200)

class imagenes(models.Model):
    nombre = models.CharField(max_length=200)
    URL = models.ImageField(upload_to='pics/%y/%m/%d/')
    cat_img = models.ForeignKey(cat_img, on_delete=models.CASCADE, null=True)

class paises(models.Model):
    nombre = models.CharField(max_length=200)
    img_bandera = models.ForeignKey(imagenes,on_delete=models.CASCADE, null=True)
    cat_img = models.ForeignKey(cat_img, on_delete=models.CASCADE, null=True)

class recetas(models.Model):
    pais = models.ForeignKey(paises,on_delete=models.CASCADE,null=True)
    nombre = models.CharField(max_length=200)
    sinopsis = models.TextField()
    ingredientes = models.TextField()
    proceso = models.TextField()
    like = models.IntegerField()
    img = models.ForeignKey(imagenes,on_delete=models.CASCADE, null=True)
    cat_img = models.ForeignKey(cat_img, on_delete=models.CASCADE, null=True)
