from things.views import ListThing, DetailThing
from django.urls import path

urlpatterns = [
    path("", ListThing.as_view(), name = "list_thing"),
    path("<int:pk>/", DetailThing.as_view(), name = "detail_thing")
]