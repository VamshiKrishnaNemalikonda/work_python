from django.shortcuts import render

# Create your views here.
# import viewsets
from rest_framework import viewsets
import json
 
# import local data
#from .serializers import NFOSerializer
#from .models import NFOModel

from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    #return JsonResponse({"message: Hi there"}, safe=False)
    process_helm_charts()
    return JsonResponse(data)


def process_helm_charts():
    print("Processing Helm charts")



# create a viewset  
#class NFOViewSet(viewsets.ModelViewSet):
    # define queryset
    #queryset = NFOModel.objects.all()
 
    # specify serializer to be used
    #serializer_class = NFOSerializer