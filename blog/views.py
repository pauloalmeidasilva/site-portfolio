from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import *

# Create your views here.
def index(request):
	#return render(request, 'blog/index.html',{})
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    conhecimentos = conhecimento.objects.filter()
    formacoes = formacao.objects.filter()
    experiencias = experiencia.objects.filter()
    projeto = portfolio.objects.filter()

    #Para exibir os 3 primeiros 
    #published_date__lte=timezone.now()).order_by('published_date')[:3]

    # Para mostrar um conjunto de blogs em um "dicionário".
    #context = {'posts': posts}

    return render(request, 'blog/index.html', {'posts': posts, 'conhecimentos': conhecimentos, 'formacoes': formacoes, 'experiencias':experiencias, 'projetos': projeto})