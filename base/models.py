from django.db import models

# Create your models here.

##### Projetos #####

class Projeto(models.Model):
	nome = models.CharField(max_length=60)
	tópico = models.CharField(max_length=60, blank=True)
	body = models.TextField(blank=True, null=True)
	image = models.ImageField(null = True, blank=True)
	def __str__(self):
		return self.nome



##### Blog #####

class Categoria(models.Model):
	nome = models.CharField(max_length=255)
	def __str__(self):
		return self.nome


class Post(models.Model):
	titulo = models.CharField(max_length=60)
	body = models.TextField( blank=True, null=True)
	criado_em = models.DateTimeField(auto_now_add=True)
	modificação = models.DateTimeField(auto_now=True)
	categorias = models.ManyToManyField('Categoria', related_name='posts')
	def __str__(self):
		return self.titulo


class Comentario(models.Model):
    autor = models.CharField(max_length=60)
    body = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    def __str__(self):
    	return self.autor
    	
