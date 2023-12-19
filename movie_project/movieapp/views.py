from django.http import HttpResponse
from django.shortcuts import render, redirect

from . models import Movie
from . form import MovieForm
# Create your views here.

def index(request):
    # Movie.objects.all().order_by(strip_tags('name'))
    # Movie.objects.all().order_by(strip_tags('desc'))
    # Movie.objects.all().order_by(strip_tags('id'))
    movie = Movie.objects.all()
    context={
        'movie_list':movie

    }
    return render(request,'index.html',context)


def detail(request,mov_id):
    movie=Movie.objects.get(id=mov_id)
    return render(request,'detail.html', {'mov':movie})


def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save()


def add_new(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save()
        return redirect('/')
    return render(request,'addmovie.html')

    return render(request,'add.html')

def update(request, id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return  redirect('/')
    return  render(request,'edit.html',{'form':form,'movie':movie})


def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
