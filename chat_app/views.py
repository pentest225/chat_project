from django.shortcuts import render,redirect
from rest_framework import viewsets
from . import  models
from .serializers import User_groupeSerializer,Ami_userSerializer,GroupeChatSerializer,User_groupeSerializer,SalonSerializer,MessageUserSerializer,UserSerializer,ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import socket
import requests


# Create your views here.

# Create your views here.


    
class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = models.User.objects.all()
    
class ProfileViewset(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = models.Profile.objects.all()

class GroupeChatViewset(viewsets.ModelViewSet):
    serializer_class = GroupeChatSerializer
    queryset = models.GroupeChat.objects.all()
    
class Ami_userViewset(viewsets.ModelViewSet):
    serializer_class = Ami_userSerializer
    queryset = models.Ami_user.objects.all()
    
class User_groupeViewset(viewsets.ModelViewSet):
    serializer_class = User_groupeSerializer
    queryset = models.User_groupe.objects.all()
    
# class Type_salonViewset(viewsets.ModelViewSet):
#     serializer_class = Type_salonSerializer
#     queryset = models.Type_salon.objects.all()
    
class SalonViewset(viewsets.ModelViewSet):
    serializer_class = SalonSerializer
    queryset = models.Salon.objects.all()
    
class MessageUserViewset(viewsets.ModelViewSet):
    serializer_class = MessageUserSerializer
    queryset = models.MessageUser.objects.all()

def index(request):
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)  
    IPAddr ='160.154.137.78'
    myUrl ='https://ipapi.com/ip_api.php?ip='+IPAddr+''
    try:
        allPcInfo =requests.get(myUrl)
        print(allPcInfo.text)
    except:
        print("Error in try to get informations ")
    print("####################SOCKET INFO ########################")  
    print("Your Computer Name is:" + hostname)    
    print("Your Computer IP Address is:" + IPAddr)
    print(myUrl)
    return render(request,'pages/index.html')

def salon(request,slog_one,slog_two):
    
    my_type_salon=None
    sal=None
    my_sal=None
    #On verifie si le slog est valide 
    if models.Profile.objects.filter(user_slug=slog_one).exists():
        my_type_salon="salon_pive"
    if models.GroupeChat.objects.filter(slug_group=slog_one).exists():
        my_type_salon="salon_groupe"
    
    #Ok le slug est valide 
    if my_type_salon is not None:
        
        if models.Salon.objects.filter(sender_one=slog_one,sender_two=slog_two).exists():
            my_sal = models.Salon.objects.get(sender_one=slog_one)
        elif models.Salon.objects.filter(sender_two=slog_one,sender_one=slog_two).exists():
            my_sal = models.Salon.objects.get(sender_two=slog_one)
        else:
            my_sal = models.Salon(sender_two=slog_one,sender_one=slog_two,type=my_type_salon)
            my_sal.save()
        
    
    if my_sal is not None:
        sal=[{"salon_id":my_sal.id,"slug_one":my_sal.sender_one,"slug_tow":my_sal.sender_two,"salon_name":my_sal.nom,"date_app":my_sal.date_add,"date_upd":my_sal.date_upd,"status":my_sal.status } ]
    
    data={
        "salon":sal
    }
    return JsonResponse(data,safe=False)


def connexion(request):
    print("################ONNEXION####################")
    
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)

    if user is not None and user.is_active:
        print("user is login")
        login(request, user)
        data={
            'is_login':True,
            'username':user.username
        }
 # page si connect
    else:
        data={
            'is_login':False,
        }
    return JsonResponse(data)

