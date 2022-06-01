from django.shortcuts import render

# from asyncio import tasks
# from multiprocessing import context
# from django.shortcuts import render

# from wolf.blogApp.models import Task

from asyncio import tasks
from django.forms import SlugField
from django.shortcuts import render
from .models import Article
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    data = Article.objects.all()
    context = {'tasks':data}
    return render(request, "article_template/index.html", context)


def detail(request, slug):
    data2 = Article.objects.get(slug=slug)
    context = {'tasks':data2}
    return render(request, 'article_template/detail.html', context)