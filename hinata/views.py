from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from register.forms import Sky
from hinata.forms import TodoForm
from .models import TdListName,Todomodel
from django.contrib.auth.decorators import login_required


# Create your views here
#at http://127.0.0.1:8000/

@login_required
#displying the todolist and should have one edit button which should take to edit Items views 
def home(request):
        user_name = request.user.username
        #getting the todomodel items of current logged in user
        info_of_user = TdListName.objects.get(name=user_name)
        items= Todomodel.objects.filter(user=info_of_user)
        todos = Todomodel.objects.all()
        return render(request, 'hinata/home.html', {'user_name':user_name, "items":items})





#creating a task list based on the user registration form
@login_required
def add(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            current_user = request.user
            info_of_user, created = TdListName.objects.get_or_create(name=current_user.username)
            new_todo = form.save(commit=False)
            new_todo.user = info_of_user
            new_todo.save()
            return redirect('/')        
        else:
            print("Something wrong with the form")
    else:
        form = TodoForm()
    return render(request, 'hinata/add.html', {'form': form})
    
def Update(request, todoname):
    get_todo = Todomodel.objects.get(task_name = todoname)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=get_todo)
        if form.is_valid():
            form.save()
            return redirect('/')
        
        
    else:
        form = TodoForm(initial={'task_name': todoname})
    return render(request, 'hinata/update.html', {'form':form})

def Delete(request,todoname):
    get_todo = Todomodel.objects.get(task_name =todoname)
    get_todo.delete()
    return redirect('/')