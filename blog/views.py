from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from blog.models import Article, Category
from django.contrib.auth.decorators import login_required
from projects.forms import ArticleForm
from django.contrib import messages
# Create your views here.

# Create your views here.



def list(request):

    # Sacar los articulos
    articles = Article.objects.all()
    # Paginar los articulos
    paginator = Paginator(articles, 8)

    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request,'articles/list.html',{
        'title': 'Inicio',
        'articles': page_articles
    })

def category(request, category_id):

    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(categories=category_id)

    return render(request,'categories/category.html',{
        'category': category,
        'articles': articles,
    })

def article(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    return render(request,'articles/detail.html',{
        'article': article,
    })

@login_required(login_url=('login'))
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            form.save_m2m()
            messages.success(request, 'El artículo ha sido publicado con éxito.')
            return redirect('list_articles')
        else:
            messages.error(request, 'Ha ocurrido un error al publicar el artículo.')
    else:
        form = ArticleForm()

    return render(request, 'articles/create_article.html', {'form': form})

    
