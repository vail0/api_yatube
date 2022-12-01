from api.views import GroupViewSet, PostViewSet
from django.urls import include, path

from rest_framework.routers import DefaultRouter

# Создаётся роутер
router = DefaultRouter()
# Вызываем метод .register с нужными параметрами
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [
    # Все зарегистрированные в router пути доступны в router.urls
    # Включим их в головной urls.py
    path('', include(router.urls)),

]
