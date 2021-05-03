"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# import DRF Router Base
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView

# import our views
from tasklist.views import GroupViewSet, UserViewSet, TaskViewSet

# Default routers for DRF
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)

auth_patterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('groups/', GroupViewSet.as_view()),
]

api_urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include(auth_patterns)),
]

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # Inyected router API
    path('api/', include(api_urlpatterns)),
]
