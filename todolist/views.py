from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.models import Task
import datetime
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# TODO: Create your views here.

@login_required(login_url='/todolist/login/')
def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def toggle_is_finished(request, id):
    task = Task.objects.get(user=request.user, id=id)
    task.is_finished = not(task.is_finished)
    task.save(update_fields = ['is_finished'])

    return HttpResponseRedirect(reverse("todolist:show_todolist"))

def delete_task (request, id):
    task = Task.objects.get(user=request.user, id=id)
    task.delete()
    return HttpResponseRedirect(reverse("todolist:show_todolist"))

@login_required(login_url="/todolist/login/")
def create_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            date=datetime.datetime.today(),
        ).save()
        return HttpResponseRedirect(reverse("todolist:show_todolist"))
    return render(request, "create-task.html")

@login_required(login_url="/todolist/login/")
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            date=datetime.datetime.today(),
        ).save()
        return HttpResponseRedirect(reverse("todolist:show_todolist"))
    return JsonResponse({'message': 'success'})

@login_required(login_url="/todolist/login/")
def show_todolist(request):
    todolist_objects = Task.objects.filter(user=request.user)

    if request.method == 'POST':
        temp = Task(user=request.user, title=request.POST.get('title'), description=request.POST.get('description'))
        temp.save()
        return JsonResponse({'message': 'success'})

    context = {
        "todolist": todolist_objects, 
        "username": request.user,
        }
    
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Akun telah berhasil dibuat!")
            return redirect("todolist:login_user")

    context = {"form": form}
    return render(request, "register.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, "Username atau Password salah!")
    context = {}
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("todolist:login_user"))
    response.delete_cookie("last_login")
    return response

