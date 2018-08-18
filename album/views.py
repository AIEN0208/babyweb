from django.shortcuts import render,redirect
from django.http import HttpResponse
from album.models import Album
from album.models import Paint
from album.models import Covered
from member.models import Member

def index(request):
    if request.COOKIES.get('id') != None:
        UserId = request.COOKIES['id']
        photos = Album.objects.filter(UserId = UserId)
        member = Member.objects.filter(id = UserId)[0]
        response = render(request, "album/index.html", locals())
    else:
        response = HttpResponse("<script>alert('請先登入才可以看到寶寶的照片喔!'); location.href = window.history.back(1) </script>")   
    
    return response

def paint(request):
    if request.COOKIES.get('id') != None:
        UserId = request.COOKIES['id']
        paints = Paint.objects.filter(UserId = UserId)
        member = Member.objects.filter(id = UserId)[0]
        response = render(request, "album/paint.html", locals())
    else:
        response = HttpResponse("<script>alert('請先登入才可以看到寶寶的作品喔!'); location.href = window.history.back(1) </script>")
    return response

def covered(request):
    UserId = request.COOKIES['id']
    member = Member.objects.filter(id = UserId)[0]
    covered = Covered.objects.filter(UserId = UserId)
    return render(request, "album/covered.html", locals())

def dalbum(request,id):
    album = Album.objects.get(id= int(id))
    album.delete()
    return redirect('/album')

def dpaint(request,id):
    paint = Paint.objects.get(id= int(id))
    paint.delete()
    return redirect('/album/paint')

def dcovered(request,id):
    covered = Covered.objects.get(id= int(id))
    covered.delete()
    return redirect('/album/covered')