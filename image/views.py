from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.views import APIView

# Create your views here.

class ImagesAPI(APIView):
    def post(self,request):
        data = ImagesSerializer(data=request.data)
        if data.is_valid():
           data.save()
           return Response(data.data,status=status.HTTP_201_CREATED) 
        else:
            return Response(data.errors,status=status.HTTP_400_BAD_REQUEST)  
    
    def get(self, request, pk=None):
        try:
            try:
                if pk is not None:  
                    data = Images.objects.get(id = pk)
                    result = ImagesSerializer(data)
                    return Response(result.data,status=status.HTTP_200_OK)
                else:
                    data = Images.objects.all()
                    result = ImagesSerializer(data, many=True)
                    return Response(result.data,status=status.HTTP_200_OK)
            except :
                message = {"error":"id not exist"}
                return Response(message,status=status.HTTP_404_NOT_FOUND)
                        
        except Exception as e:
            print(e)
            return Response(e,status=status.HTTP_404_NOT_FOUND)
       
    def put(self, request, pk):
        try:
            old_data = Images.objects.get(id=pk)
            result = ImagesSerializer(old_data, data = request.data)
            if result.is_valid():
                result.save()
                message = {"data":result.data}
                return Response(message,status=status.HTTP_200_OK)
        except Exception as e:
            message = {"error":"id not exist"}
            print('errors:',e)
            return Response(message,status=status.HTTP_404_NOT_FOUND)
        
    def patch(self,request ,pk):
        try:
            old_data = Images.objects.get(id=pk)
            result = ImagesSerializer(old_data, data = request.data, partial=True)
            if result.is_valid():
                result.save()
                message = {"data":result.data}
                return Response(message,status=status.HTTP_200_OK)
        except Exception as e:
            message = {"error":"id not exist"}
            print('errors:',e)
            return Response(message,status=status.HTTP_404_NOT_FOUND)
          
    def delete(self, request, pk):
        try:
            data = Images.objects.get(id=pk).delete()
            return Response({'msg':'data is deleted successfully'},status=status.HTTP_200_OK)   
        
        except Images.DoesNotExist:
            return Response({'msg':'data is not found'},status=status.HTTP_404_NOT_FOUND)


