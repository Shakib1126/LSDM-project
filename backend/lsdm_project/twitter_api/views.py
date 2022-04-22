from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import twitter_data
from .serializers import twitter_dataSerializer
from .extract_data import extractData





class tweetList(APIView):


    def get(self,request):
        try:
            data = twitter_data.objects.all()
            serializer = twitter_dataSerializer(data, many=True)
            return Response(serializer.data)
        except:
            return HttpResponse("Some Technical error occured!", status = 404)