from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from asosiy.views import *

router = DefaultRouter()
router.register("ombor", OmborModelViewSet)
router.register("maxsulot", MaxsulotModelViewSet)
router.register("mijoz", MijozModelViewSet)
router.register("cd ", StatistikaModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('token_olish/', TokenObtainPairView.as_view()),
    path('token_yangilash/', TokenRefreshView.as_view()),
]
