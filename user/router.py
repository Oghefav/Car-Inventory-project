from rest_framework import routers
from user.viewset import CustomUserViewSet,AdminLoginViewSet, AdminRegisterViewSet
router = routers.DefaultRouter()

router.register(r'User',CustomUserViewSet,  basename='User')
router.register(r'admin_register', AdminRegisterViewSet, basename='Admin Register')
router.register(r'admin_login', AdminLoginViewSet, basename='Admin Login')

urlpatterns = [
    *router.urls
]