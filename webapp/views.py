from django.shortcuts import render
from webapp.models import City, theatre, show
from webapp.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def moviepicker(request):
    city_name = request.GET.get( 'city')
    city = City.objects.get(city_name=city_name)
    show_queryset = show.objects.filter(city=city)
    serializer_data=showfetch(show_queryset, many=True)
    return Response(serializer_data.data, status=status.HTTP_201_CREATED)




