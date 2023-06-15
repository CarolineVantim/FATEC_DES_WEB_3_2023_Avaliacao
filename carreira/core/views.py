from django.shortcuts import render
from .models import CadastroModel
from .forms import CadastroForm

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            CadastroModel.objects.create(**form.cleaned_data)
            contexto = {
                'cadastroPresenca': True
            }
            return render(request, "cadastroPresenca.html", contexto)
        else:
            contexto = {'form': form}
            return render(request, "cadastroPresenca.html", contexto)
    else:
        contexto = {'form': CadastroForm}
        return render(request, "cadastroPresenca.html", contexto)

def listar(request):
    cadastrados = CadastroModel.objects.all() 
    if len(cadastrados)>0:
        contexto = {
            'cadastrados': cadastrados
        }
        return render(request, 'listar.html', contexto)
    else:
        contexto = {
            'cadastrados': False
        }
        return render(request, 'listar.html', contexto)