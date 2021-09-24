from django.shortcuts import render
from .models import Projeto, Post, Comentario
from .forms import ComentarioForm

# Create your views here.

##### Apresentação #####
def home(request):
	projetos = Projeto.objects.all()
	context = {'projetos':projetos}
	return render(request, 'base/home.html', context)

def projetopage(request, pk):
	projeto = Projeto.objects.get(pk=pk)
	context = {'projeto':projeto}
	if pk == 3:
		return render(request, 'base/projetopagel.html', context)
	return render(request, 'base/projetopage.html', context)

##### Blog #####
def blog_index(request):
	posts = Post.objects.all().order_by('-criado_em')
	context = {'posts':posts}
	return render(request, "base/blog_index.html", context)

def blog_categoria(request, categoria):
	posts = Post.objects.filter(categorias__nome__contains=categoria).order_by('-criado_em')
	context = {'categoria': categoria,
	'posts': posts}
	return render(request, "base/blog_categoria.html", context)


def blog_detail(request, pk):
	post = Post.objects.get(pk=pk)

	form = ComentarioForm()
	if request.method == 'POST':
		form = ComentarioForm(request.POST)
		if form.is_valid():
			comentario = Comentario(
				autor=form.cleaned_data["autor"],
				body=form.cleaned_data["body"],
				post=post
				)
			comentario.save()


	comentarios = Comentario.objects.filter(post=post)
	context = {"post":post,
	"comentarios":comentarios,
	"form": form}
	return render (request, "base/blog_detail.html", context)


##### Henry James #####
def henryjames(request):
	return render (request, "base/henryjames.html")