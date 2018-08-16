from django.shortcuts import render,redirect
from django.http import HttpResponse
from album.models import Album
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
