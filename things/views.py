from things.serializers import ThingSerializer
from things.models import Thing
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
# Create your views here.

class ListThing(ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    
class DetailThing(RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer