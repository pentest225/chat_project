from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  # 1 user <---> 1 profil
    #Champs suplementaires
    contacts = models.CharField(max_length=30, null=True)
    image = models.ImageField(upload_to='profile/', default='useravatar.png')
    actu = models.CharField(max_length=50)
    user_slug = models.CharField( max_length=255,unique=True,null=True)
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    @property
    def get_slog(self, *args, **kwargs):
        self.user_slug = self.contacts +'_slog_'+ str(self.id)
        self.save()
   
class GroupeChat(models.Model):
    nom=models.CharField(max_length=50)
    superAdmin=models.ForeignKey(User,on_delete=models.CASCADE,related_name='super_admin')
    description=models.TextField()
    logo = models.ImageField()
    slug_group = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.nom
    
    @property
    def get_slog(self, *args, **kwargs):
        self.slug_group = self.nom +'_slog_'+ str(self.id)
        self.save()
        
class Ami_user(models.Model):
    user_one =models.ForeignKey(User,related_name='user_ami_one',on_delete=models.CASCADE,null=True)
    user_two =models.ForeignKey(User,related_name='user_ami_two',on_delete=models.CASCADE,null=True)
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
def __str__(self):
    return self.nom

class User_groupe(models.Model):
    groupe = models.ForeignKey(GroupeChat,on_delete=models.CASCADE,related_name='groupe_user')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    is_admin = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.groupe.nom



class Salon(models.Model):
    sender_one = models.CharField(max_length=255,null=True)
    sender_two = models.CharField(max_length=255,null=True)
    type = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    @property
    def get_slog(self):
        self.nom ='salon_'+ str(self.id)
        self.save()
        return self.nom
        
    def __str__(self):
        return self.nom
    

class MessageUser(models.Model):
    sender =  models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender_msg')
    salon = models.ForeignKey(Salon,on_delete=models.CASCADE,related_name='salon_msg')
    message = models.TextField()
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.sender
    

