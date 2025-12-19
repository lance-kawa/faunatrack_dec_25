"""
URL configuration for pythagore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls
from rest_framework.routers import DefaultRouter
from faunatrack.api import EspeceViewset, HelloWorldView, ObservationViewset, ProjectViewset
from faunatrack.views import ObservationCreate, ObservationList, ObservationUpdate, hello_world
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
router = DefaultRouter()
router.register(r'observations', ObservationViewset, basename='observation')
router.register(r'especes', EspeceViewset, basename='espece')
router.register(r'projects', ProjectViewset, basename='project')
# Pas de slash en début d'urls !
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world, name="home" ),
    path("observations/", ObservationList.as_view(), name="observations_list"),
    path("observations/create/", ObservationCreate.as_view(), name="observations_add"),
    path("observations/<uuid:pk>/update/", ObservationUpdate.as_view(), name="observations_update"),
    path("auth/", include("django.contrib.auth.urls")),
    # path('api/', include('rest_framework.urls')),
    path('api/hello-world/', HelloWorldView.as_view(), name="hello_world"),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + debug_toolbar_urls()
