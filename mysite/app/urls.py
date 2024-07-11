from django.urls import path, include
from rest_framework.routers import DefaultRouter

from mysite import app
from .views import UserViewSet, InterestViewSet, ChatMessageViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'interests', InterestViewSet)
router.register(r'chatmessages', ChatMessageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
from django.urls import path, include
from rest_framework.authtoken import views as drf_views

urlpatterns = [
    ...,
    path('api/auth/', include('rest_framework.urls')),
    path('api/auth/token/', drf_views.obtain_auth_token),
    path('api/register/', app.views.RegisterView.as_view()),  # custom registration view
...
]



