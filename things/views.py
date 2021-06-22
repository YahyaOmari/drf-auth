from things.serializers import ThingSerializer
from things.models import Thing
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .permissions import IsOwnerOrReadOnly
# Create your views here.

class ListThing(ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    
class DetailThing(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer