from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie_details
from .form import FormMovies
# Create your views here.


def index(request):
    movie=movie_details.objects.all()
    context={
               'movie_list':movie
            }
    return render(request,'index.html',context)
def details(request,movie_id):
    movie=movie_details.objects.get(id=movie_id)
    return render(request,'details.html',{'movie':movie})
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('movie_name')
        des=request.POST.get('movie_desc')
        Movie_year=request.POST.get('year')
        price=request.POST.get('Ticket_price')
        image=request.FILES['img']
        movie_db=movie_details(movie_name=name,movie_desc=des,year=Movie_year,Ticket_price=price,img=image)
        movie_db.save()
    return render(request,'add_movie.html')
def update(request,id):
    movies=movie_details.objects.get(id=id)
    form=FormMovies(request.POST or None, request.FILES, instance=movies)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movie':movies})
def delete(request,id):
    if request.method=='POST':
        movie=movie_details.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
