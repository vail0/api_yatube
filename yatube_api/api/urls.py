from api.views import CommentViewSet, GroupViewSet, PostViewSet
from django.urls import include, path

from rest_framework.routers import DefaultRouter

# Создаётся роутер
router = DefaultRouter()
# Вызываем метод .register с нужными параметрами
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)

# При регистрации эндпоинтов с таким URL-префиксом
router.register(r'posts/(?P<post_id>[\d]+)/comments', CommentViewSet,
                basename='post_comments')
# ...вьюсет AnyViewSet будет получать на обработку все запросы с адресов
# ...и подобных, ограниченных маской регулярного выражения.

urlpatterns = [
    # Все зарегистрированные в router пути доступны в router.urls
    path('api/v1/', include(router.urls)),
]
