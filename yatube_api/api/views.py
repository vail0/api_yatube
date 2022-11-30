# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# from posts.models import Post
# from .serializers import PostSerializer


# # View-функция cat_list() будет обрабатывать только запросы GET и POST,
# # запросы других типов будут отклонены,
# # так что в теле функции их можно не обрабатывать
# @api_view(['GET', 'POST'])
# def post_list(request):
#     if request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     cats = Post.objects.all()
#     serializer = PostSerializer(cats, many=True)
#     return Response(serializer.data)
