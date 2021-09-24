from django.contrib import admin
from .models import Projeto, Post, Categoria, Comentario

# Register your models here.
admin.site.register(Projeto)
admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Comentario)