from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from datetime import date
from django.shortcuts import get_object_or_404

from .forms import RoomForm
from .models import Room, Topic


def login_page(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Username or password is incorrect")

    return render(request, "wydarzenia/login_register.html", {"page": page})


def logout_user(request):
    logout(request)
    return redirect("home")


def register_page(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.warning(request, "error rejestracji")

    return render(request, "wydarzenia/login_register.html", {"form": form})


def home(request):
    room_list_by_date = Room.objects.filter(
        date__gte=date.today()
    ).order_by("date")
    topics = Topic.objects.all()
    room_count = room_list_by_date.count()
    return render(request, "wydarzenia/home.html", {"topics": topics, "room_list": room_list_by_date})


def history(request):
    room_list_by_date = Room.objects.filter(
        date__lt=date.today()
    ).order_by("date")
    topics = Topic.objects.all()
    context = {
        "topics": topics,
        "room_list": room_list_by_date,
    }
    return render(request, "wydarzenia/history.html", {"topics": topics, "room_list": room_list_by_date})


def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created')
    return render(request, "wydarzenia/room.html", {"room": room, 'room_messages': room_messages})


def profile(request, pk):
    profile = get_object_or_404(User, pk=pk)
    room_list_by_date = Room.objects.filter(
        host=pk
    ).order_by("date")
    topics = Topic.objects.all()
    context = {
        "profile": profile,
        "topics": topics,
        "room_list": room_list_by_date,
    }
    return render(request, "wydarzenia/profile.html", context)


@login_required(login_url="login")
def create_room(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "wydarzenia/room_form.html", {"form": form})


@login_required(login_url="login")
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "wydarzenia/room_form.html", {"form": form})


@login_required(login_url="login")
def delete_room(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, "wydarzenia/delete.html", {"obj": room})
