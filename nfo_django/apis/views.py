from django.shortcuts import render

# Create your views here.
# import viewsets
from rest_framework import viewsets
 
# import local data
from .serializers import NFOSerializer
from .models import NFOModel
 
# create a viewset
 
 
class NFOViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = NFOModel.objects.all()
 
    # specify serializer to be used
    serializer_class = NFOSerializer