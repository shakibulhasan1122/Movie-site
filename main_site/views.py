from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import ListView,DetailView,TemplateView
from . models import Genre
from . models import MoviesLink
from . models import Category


def HomeView(request):
    movie=MoviesLink.objects.all()
    menu=Category.objects.all()
    genre=Genre.objects.all()
    #paginator=Paginator(articles,2)
    #page=request.GET.get('page')

    #articles=paginator.get_page(page)
    context={'movie':movie,'menu' :menu,'genre' :genre}
    return render(request,'home.html',context)

class MovieDetailView(DetailView):
    model=MoviesLink
    template_name='movie_download.html'
    context_object_name= 'movie'
    

    
        
    