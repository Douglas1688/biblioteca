from django.db import models
from django.db.models.deletion import CASCADE

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    apellidos = models.CharField(max_length=220,blank=False, null=False)
    nacionalidad = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    fecha_creacion = models.DateField('Fecha de creación', auto_now=True, auto_now_add = False)
    estado = models.BooleanField('Estado',default=True)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __str__(self) -> str:
        return self.nombre

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=255, blank=False, null=False)
    fecha_publicacion = models.DateField('Fecha de publicación', blank=False, null=False)
    fecha_creacion = models.DateField('Fecha de creación', auto_now=True, auto_now_add = False)
    estado = models.BooleanField('Estado',default=True)
    autor_id = models.ForeignKey(Autor,null=True,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self) -> str:
        return self.titulo

 