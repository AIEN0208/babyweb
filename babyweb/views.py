from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from member.models import Member
from album.models import Album
import datetime
import album.serializers as serializers
from rest_framework import viewsets

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = serializers.AlbumSerializer


def login(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        member = Member.objects.filter(UserEmail = email, UserPassword = password).values('UserName', 'id')
            
        if member:
            response = HttpResponse('<script>alert("登入成功"); location.href = window.history.back(2)</script>')
            if 'rememberme' in request.POST:
                expiredate = datetime.datetime.now() + datetime.timedelta(days=3)
                response.set_cookie("name", member[0]["UserName"], expires = expiredate)
                response.set_cookie("id", member[0]["id"], expires = expiredate)
            
            else:
                response.set_cookie("name", member[0]["UserName"])
                response.set_cookie("id", member[0]["id"])
        else:
            response = HttpResponse("<script>alert('登入失敗'); location.href = window.history.back(2) </script>")    
        
        return response


   
    