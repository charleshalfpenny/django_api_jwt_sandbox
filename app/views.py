from django.shortcuts import render, HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ParseError

from rest_framework.permissions import IsAuthenticated    # for JWT toke authentication


from .serializers import *
from .models import *
from .filters import *


def index(request):
  return HttpResponse("<h1>API JSW Sandbox</h1")


# JWT Testing
class ProtectedView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    return Response({"message": "You are authenticated!"})  


# Employee

class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer   
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmployeeFilter

class EmployeeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer  


  