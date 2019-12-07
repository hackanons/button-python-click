from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE
from django.core.files.storage import FileSystemStorage

def button(request):

    return render(request,'home.html')

def output(request):
    data=requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request,'home.html',{'data':data})

def external(request):
    inp= request.POST.get('param')
    image=request.FILES['image']
    print("image is ",image)
    fs=FileSystemStorage()
    filename=fs.save(image.name,image)
    fileurl=fs.open(filename)
    templateurl=fs.url(filename)
    print("file raw url",filename)
    print("file full url", fileurl)
    print("template url",templateurl)
    out= run([sys.executable,'//mnt//e//work//button-python-click//html button external python script//test.py',inp],shell=False,stdout=PIPE)
    image= run([sys.executable,'//mnt//e//work//button-python-click//html button external python script//image.py',str(fileurl),str(filename)],shell=False,stdout=PIPE)
    print(out)
    print(image.stdout)
    return render(request,'home.html',{'data':out.stdout,'raw_url':templateurl,'edit_url':image.stdout})

