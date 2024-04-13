from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class TaskUserView(View):
    def home(request):
        return render(request, 'index.html')

    def signup(self,request, *args, **kwargs):
        if request.method == 'GET':
            print('Enviando formulario')
        else:
            print(request.POST)
            print('Obteniendo datos')
        context={
            'form': UserCreationForm
        }
        return render(request, 'tasks_users.html', context)
