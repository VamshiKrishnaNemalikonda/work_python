from django.shortcuts import render
import pyhelm
from kubernetes import client

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
    # Load the Helm chart
    chart = pyhelm.load_chart('./my-chart')

    # Get the chart's values
    values = chart.values

    # Get the chart's templates
    templates = chart.templates

    # Render the chart's templates
    rendered_templates = chart.render_templates(values)

    # Get the chart's manifest
    manifest = chart.manifest

    # Deploy the chart to Kubernetes
    client.CoreV1Api().create_namespaced_deployment(namespace='default', body=manifest)



# create a viewset  
#class NFOViewSet(viewsets.ModelViewSet):
    # define queryset
    #queryset = NFOModel.objects.all()
 
    # specify serializer to be used
    #serializer_class = NFOSerializer