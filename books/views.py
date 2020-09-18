from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView


class IndexView(APIView):

    def get(self, request, *args, **kwargs):
        return HttpResponse(111111)
