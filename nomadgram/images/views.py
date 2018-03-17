from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
class ListAllImages(APIView):

    def get(self, request, format=None):

        all_images = models.Image.objects.all() # Image모델의 모든 이미지를 가져온다.

        # serializer는 class / 시리얼라이저를 통해 data라는 이름의 변수에 저장
        serializer = serializers.ImageSerializer(all_images, many=True) # many=True를 안써주면 1개만 변환

        return Response(data=serializer.data)

class ListAllComments(APIView):

    def get(self, request, format=None):

        all_comments = models.Comment.objects.all()

        serializer = serializers.CommentSerializer(all_comments, many=True)

        return Response(data=serializer.data)

class ListAllLikes(APIView):

    def get(self, request, format=None):

        all_likes = models.Like.objects.all()

        serializer = serializers.LikeSerializer(all_likes, many=True)

        return Response(data=serializer.data)