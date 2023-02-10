from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    listaArticulos=[]
    for ele in range(20):
        listaArticulos.append('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the {}s'.format(ele))
    context={'lista':listaArticulos}
    return render(request,'index.html',context)

def uno(request):
    return render(request, '1.html',{})