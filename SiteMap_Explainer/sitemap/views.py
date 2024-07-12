from django.shortcuts import render, get_object_or_404
from .models import Article

def index(request):
    return render(request, 'sitemap/index.html')

def about(request):
    return render(request, 'sitemap/about.html')

def contact(request):
    return render(request, 'sitemap/contact.html')

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'sitemap/article_list.html', {'articles': articles})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'sitemap/article_detail.html', {'article': article})
