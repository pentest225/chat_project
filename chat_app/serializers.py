from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token



        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password':{'write_only':True,'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


    

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = models.Profile
        fields = '__all__'
    def create(self, validated_data):
        profile = models.Profile.objects.create(**validated_data)
        return profile

class GroupeChatSerializer(serializers.ModelSerializer):
    super_admin = UserSerializer(many=True,required=False)
    class Meta:
        model = models.GroupeChat
        fields = '__all__'
        
class Ami_userSerializer(serializers.ModelSerializer):
    user_one = ProfileSerializer(many=False,required=True)
    user_two = ProfileSerializer(many=False,required=True)
    class Meta:
        model = models.Ami_user
        fields = '__all__'

class User_groupeSerializer(serializers.ModelSerializer):
    groupe_user = GroupeChatSerializer(many=True,required=False)
    superAdmin = UserSerializer(many=False)
    user = UserSerializer(many=True,required=False)
    class Meta:
        model = models.User_groupe
        fields = '__all__'

# class Type_salonSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = models.Type_salon
#         fields = '__all__'

    
class SalonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Salon
        fields = '__all__'
        
class MessageUserSerializer(serializers.ModelSerializer):
    sender_msg = UserSerializer(many=True,required=True)
    salon_msg =  SalonSerializer(many=True,required=True)
    class Meta:
        model = models.MessageUser
        fields = '__all__'