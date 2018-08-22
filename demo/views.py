from django.shortcuts import render

# Create your views here.
def linebot(request):
    return render(request,'demo/linebot.html',locals())

def eyesnose(request):
    return render(request,'demo/eyesnose.html',locals())

def sound(request):
    return render(request,'demo/sound.html',locals())

def areas(request):
    return render(request,'demo/areas.html',locals())

def emotion(request):
    return render(request,'demo/emotion.html',locals())

def paint(request):
    return render(request,'demo/paint.html',locals())