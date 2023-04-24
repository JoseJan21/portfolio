from django.urls import path, include
from . import views
import pages.views
import blog.views


urlpatterns = [
    path('generator/', views.generator, name='generator'),
    path('generator/password/', views.password, name='password'),
    path('pagina/about-web', views.web, name='web'),
    path('pagina/<str:slug>', pages.views.page, name='page'),
    path('pagina/', blog.views.list, name='list_articles'),
    path('pagina/categoria/<int:category_id>', blog.views.category, name='category'),
    path('pagina/article/<int:article_id>', blog.views.article, name='article'),
    path('pagina/register/', views.register_page, name='register'),
    path('pagina/login/', views.login_page, name='login'),
    path('pagina/logout/', views.logout_page, name='logout'),
    path('pagina/create-article/', blog.views.create_article, name='create_article'),
    path('todolist/', include('todolist.urls'), name='todolist'),
]