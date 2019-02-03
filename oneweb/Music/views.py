from django.http import HttpResponse
from .models import Album
from django.shortcuts import render

def index(request):
    all_albums=Album.objects.all()
    context ={'all_albums':all_albums}
    return render(request,'Music/index.html',context)

def detail(request,album_id):
    return HttpResponse("<h2> Details for album id:"+str(album_id)+"<h2>")