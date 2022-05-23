from django.urls.conf import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserApiViewSet, UserView, GroupView

router_user = DefaultRouter()

router_user.register(prefix="users", basename="users", viewset=UserApiViewSet)

urlpatterns = router_user.urls


urlpatterns += [
    path("groups/", GroupView.as_view()),
    path("auth/me/", UserView.as_view()),
    path("auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
