from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.http import HttpResponseRedirect

def index(request):
    articles = models.Artical.objects.all()
    return render(request,'blog/index.html',{'articles':articles})

def article_page(request,article_id):
    article = models.Artical.objects.get(pk =article_id)
    return render(request,'blog/article_page.html',{'article':article})

def edit_page(request,article_id):
    if str(article_id) == '0':
        return render(request,'blog/edit_page.html')
    article = models.Artical.objects.get(pk=article_id)
    return render(request,'blog/edit_page.html',{'article':article})

def edit_action(request):
    title = request.POST['title']
    content = request.POST['content']
    article_id = request.POST['article_id']
    if article_id == '0':
        models.Artical.objects.create(title=title,content=content)
        articles = models.Artical.objects.all()
        return HttpResponseRedirect('/blog/index')
    article = models.Artical.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request,'blog/article_page.html',{'article':article})