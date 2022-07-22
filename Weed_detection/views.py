from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from Weed_detection.h5_model import detection
from h5_model import *

def index(request):
    return render(request, "index.html")

#def detection(request):
#    if request.method =='post':
 #       return render(request,"upload.html")
    
def upload(request):
    context={}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name =fs.save(uploaded_file.name, uploaded_file)
        context['url'] =fs.url(name)

        path_var = f"media/{uploaded_file}"
        detection(path_var)
    
    return render(request,'upload.html',context)


        


def showAllimages(request):
    return render(request, "showAllimages.html")