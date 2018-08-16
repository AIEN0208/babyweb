from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def logout(request):
    response = HttpResponse("<script>alert('登出成功'); location.href = '/'</script>")
    response.delete_cookie('name')
    response.delete_cookie('id')
    return response
