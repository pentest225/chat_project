import graphene
from graphene import relay, ObjectType ,Mutation
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User
from graphene_django.filter import DjangoFilterConnectionField
from . import models


class UserNode(DjangoObjectType):
    class Meta:
        fields = "__all__"
        model=models.User
        filter_fields = {
            'username':['exact',],
        }
        interfaces =(relay.Node,)
    
    
class UserMutatons(graphene.Mutation):
    user=graphene.Field(UserNode)
    class Arguments:
        username=graphene.String(required=True)
        id=graphene.ID()
        
    def mutate(self, info, username, id):
        myUser = User.objects.get(pk=id)
        myUser.username = username
        myUser.save()
    # Notice we return an instance of this mutation
        return UserMutatons(user=myUser)
        

class ProfileNode(DjangoObjectType):
    class Meta:
        model=models.Profile
        filter_fields = ['user', 'contacts']
        interfaces =(relay.Node,)

# class ProfileMutations(graphene.Mutation):
#     profile=graphene.Field(ProfileNode)
    
#     class Arguments:
#         user = graphene.ID()
#         contacts =graphene.String()
#         actu = graphene.String()
    
#     class mutate(self,info,**kwargs):
#         user = kwargs.get('user') or None
#         contacts = kwargs.get('contacts') or None
#         actu = kwargs.get('actu') or 
class GroupeChatNode(DjangoObjectType):
    class Meta:
        model=models.GroupeChat
        fields = "__all__"
        filter_fields = {
            'nom':['exact',],
        }
        interfaces =(relay.Node,)
        
        
class Ami_userNode(DjangoObjectType):
    class Meta:
        model=models.Ami_user
        filter_fields = {
            'user_one':['exact',]
            }
        interfaces =(relay.Node,)
        
        
    
class User_groupeNode(DjangoObjectType):
    class Meta:
        model=models.User_groupe
        filter_fields = {
            'groupe':['exact',]
        }
        interfaces =(relay.Node,)
        
        
class SalonNode(DjangoObjectType):
    class Meta:
        model=models.Salon
        filter_fields = {
            'sender_one':['exact',],
            'sender_two':['exact',]
        }
        interfaces =(relay.Node,)
        
class MessageUserNode(DjangoObjectType):
    class Meta:
        model=models.MessageUser
        filter_fields = {
                'sender':['exact',]
            }
        interfaces =(relay.Node,)
        
class Query(ObjectType):
    user = relay.Node.Field(UserNode)
    all_user = DjangoFilterConnectionField(UserNode)

    profile = relay.Node.Field(ProfileNode)
    all_profiles = DjangoFilterConnectionField(ProfileNode)
    
    groupe = relay.Node.Field(GroupeChatNode)
    all_groupes = DjangoFilterConnectionField(GroupeChatNode)
    
    ami_user = relay.Node.Field(Ami_userNode)
    all_ami_users = DjangoFilterConnectionField(Ami_userNode)
    
    user_groupe = relay.Node.Field(User_groupeNode)
    all_user_groupes = DjangoFilterConnectionField(User_groupeNode)
    
    user_groupe = relay.Node.Field(User_groupeNode)
    all_user_groupes = DjangoFilterConnectionField(User_groupeNode)
    
    salon = relay.Node.Field(SalonNode)
    all_salons = DjangoFilterConnectionField(SalonNode)
    
    messageUser = relay.Node.Field(MessageUserNode)
    all_messageUsers = DjangoFilterConnectionField(MessageUserNode)