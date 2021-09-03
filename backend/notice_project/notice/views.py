import json
import re
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from .serializers import CreateNoticeSerializer, CommentReactionSerializer,EditNoticeSerializer
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.
class CreateNoticeView(views.APIView):

    def post(self, request):
        serializer = CreateNoticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentReactionAPIView(views.APIView):

    def put(self, request):
        serializer = CommentReactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "data": serializer.data,
                "message": "Your have successfully updated your reaction"
            })
        return Response({
                "success": False,
                "data": serializer.data,
                "message": "Your hreaction could not be updated"
            })


    def patch(self, request):
        serializer = CommentReactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "data": serializer.data,
                "message": "Your have successfully updated your reaction"
            })
        return Response({
                "success": False,
                "data": serializer.data,
                "message": "Your reaction could not be updated"
            })


notices = [
    {
        'id': 1,
        'title': "Test",
        'text': "Basis test", 
        'photo_url': "cdn.zuri.chat",
        'video_url':"cdn2.zuri.chat",
        'audio_url':"cdn3.zuri.chat",
    },
    {
        'id': 2,
        'title': "Test2",
        'text': "Basis test", 
        'photo_url': "cdn.zuri.chat",
        'video_url':"cdn2.zuri.chat",
        'audio_url':"cdn3.zuri.chat",
    }
]

@api_view(['PUT'])
def update_notice(request, notice_id):
    notice = None
    for tk in notices:
        if(tk['id'] == notice_id):
            notice = tk
    if(notice != None): 
        if(request.method == 'PUT'):
            serialiser = EditNoticeSerializer(notice, data=request.data)
            if(serialiser.is_valid()):
                notices.remove(notice)
                notices.append(request.data)
            return Response(request.data, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Notice not found'}, status=status.HTTP_404_NOT_FOUND)




