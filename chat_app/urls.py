from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'allUser', views.UserViewset, basename='allUser')
router.register(r'allProfile', views.ProfileViewset, basename='allProfile')
router.register(r'allGroupe', views.GroupeChatViewset, basename='allGroupe')
# router.register(r'typeSalon', views.Type_salonViewset, basename='tyoeSalon'),
router.register(r'allSalon', views.SalonViewset, basename='allSalon')
router.register(r'allMessage', views.MessageUserViewset, basename='allMessage')
router.register(r'allAmi', views.Ami_userViewset, basename='allAmi')
urlpatterns = [
    path('chat', views.index,name='index'),
    path('salon/<str:slog_one>/<str:slog_two>', views.salon,name='salon'),
    path('login', views.connexion,name='login'),
    
]

urlpatterns += router.urls