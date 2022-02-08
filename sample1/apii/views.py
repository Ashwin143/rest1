# from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework.request import  Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

# @api_view()
# def usersApi(request):
#     users=[{
#         "name":"ashwin",
#         "language":"malayalam"
#     }]
#     return Response(users)

class Student:
    def __init__(self,name ,roll ,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
