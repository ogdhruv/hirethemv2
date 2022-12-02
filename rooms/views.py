from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from rooms.forms import RoomForm
from rooms.models import Message, Room
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def rooms(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "rooms/rooms.html", context)


@login_required
def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by("-created")
    participants = room.participants.all()
    if request.method == "POST":
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get("body"),
        )
        room.participants.add(request.user)
        return redirect("room", pk=room.id)

    context = {
        "room": room,
        "room_messages": room_messages,
        "participants": participants,
    }
    return render(request, "rooms/room.html", context)


@user_passes_test(lambda u: u.is_staff)
def createRoom(request):
    form = RoomForm()
    # process data from form
    if request.method == "POST":
        form = RoomForm(request.POST,request.FILES)
        if form.is_valid():
            # the below line will save the form data in model Room
            form.instance.host = request.user
            form.save()
            return redirect("all_rooms")
    context = {"form": form}
    return render(request, "rooms/room_form.html", context)


@user_passes_test(lambda u: u.is_staff)
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("all_rooms")
    context = {"form": form}
    return render(request, "rooms/room_form.html", context)


@user_passes_test(lambda u: u.is_staff)
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect("all_rooms")
    return render(request, "rooms/delete_room.html", {"obj": room})
