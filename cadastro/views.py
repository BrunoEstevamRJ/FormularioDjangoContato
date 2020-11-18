from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Cliente

def index(request):
    if request.method=='POST':
        cliente=Cliente()
        name=request.POST.get('name')
        telefone=request.POST.get('telefone')
        email=request.POST.get('email')
        menssagem=request.POST.get('menssagem')
        cliente.nome=name
        cliente.telefone=telefone
        cliente.email=email
        cliente.menssagem=menssagem
        cliente.save()
        return HttpResponse("<h1>Obrigado pelo Contato</h1>")

    return render(request,'index.html')

