from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, InterestViewSet, ChatMessageViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'interests', InterestViewSet)
router.register(r'chatmessages', ChatMessageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

