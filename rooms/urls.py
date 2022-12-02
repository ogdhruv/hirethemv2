from django.urls import path
from .views import createRoom, rooms, room, updateRoom, deleteRoom

urlpatterns = [
    path("", view=rooms, name="all_rooms"),
    path("?=<int:pk>/", view=room, name="room"),
    path("create-room/", view=createRoom, name="createroom"),
    path("?=<int:pk>/update-room/", view=updateRoom, name="updateroom"),
    path("?=<int:pk>/delete-room/", view=deleteRoom, name="deleteroom"),
]
