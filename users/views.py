from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from .permissions import IsStaffUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class AdminPanelView(APIView):
    authentication_classes  = [TokenAuthentication]
    permission_classes = [IsStaffUser]

    def get(self, request):
        return Response({"message":"Admin Panel"})
    
    #a user who is not a staff can easily access this view why?
    
class UserView(APIView):
    authentication_classes =[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"message":"Customer Panel"})