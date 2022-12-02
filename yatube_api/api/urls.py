from api.views import CommentViewSet, GroupViewSet, PostViewSet
from django.urls import include, path

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)

router.register(r'posts/(?P<post_id>[\d]+)/comments', CommentViewSet,
                basename='post_comments')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
