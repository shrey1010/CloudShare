from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FileListSerializer
# Create your views here.
class HandleFileView(APIView):
    
    def POST(self, request, *args, **kwargs):
        try:
            data = request.data
            seralizer = FileListSerializer(data = data) 

            if seralizer.is_valid():
                seralizer.save()
                return Response({
                    'status':200,
                    'message':'files Uploaded successfully',
                })
            
            return Response({
                'status': 400,
                'message': 'something went wrong',
                'data': seralizer.errors,
            })
        
        except Exception as e:
            print(e)
            

