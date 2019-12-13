from django.contrib import admin
from .import models
from django.utils.safestring import mark_safe
# Register your models here.

#register inline
# class SousCategorieInline(admin.TabularInline):
#     model = models.SousCategorie 
#     extra = 0

    
@admin.register(models.Profile)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('view_image','user','contacts','user_slug','get_slog','status','date_add','date_upd') 
    list_filter = ('status','date_add','date_upd')#les standard ou les foreignKey
    search_fields = ('user',)#dois etre dans liste display; ne pas metres de stadard; prend le charField ou les relations 
    list_display_links = ('user','contacts')# tous les elements squf les standards
    list_per_page = 3
    ordering = ['user']
    date_hierarchy = 'date_add'
    # inlines = [SousCategorieInline]
    readonly_fields=['detaile_image']
    
    actions = ('active','deactive')
    
    def active(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,'la selections a été active avec seccès')
    active.short_description = 'active l\'utilisateur  sélectionée '
    
    def deactive(self,request,queryset):
        queryset.update(status=False)
        self.message_user(request,'la selections a ete désactive avec seccès')
    deactive.short_description = 'deactivé les categorie sélectionée '
    
    def view_image(self,obj):
        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.image.url))
    
    def detaile_image(self,obj):
        return mark_safe('<img src="{url}" width="300px" height="300px" />'.format(url=obj.image.url))
    
@admin.register(models.GroupeChat)

class GroupeChatAdmin(admin.ModelAdmin):
    list_display = ('nom','superAdmin','description','logo','status','date_add','date_upd') 
    list_filter = ('status','date_add','date_upd')#les standard ou les foreignKey
    search_fields = ('nom',)#dois etre dans liste display; ne pas metres de stadard; prend le charField ou les relations 
    list_display_links = ('nom','superAdmin')# tous les elements squf les standards
    list_per_page = 3
    ordering = ['nom']
    date_hierarchy = 'date_add'
    # inlines = [SousCategorieInline]
    readonly_fields=['detaile_image']
    
    actions = ('active','deactive')
    
    def active(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,'la selections a été active avec seccès')
    active.short_description = 'active du groupe  sélectionée '
    
    def deactive(self,request,queryset):
        queryset.update(status=False)
        self.message_user(request,'la selections a ete désactive avec seccès')
    deactive.short_description = 'deactivé les groupe sélectionée '
    
    def view_image(self,obj):
        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.logo.url))
    
    def detaile_image(self,obj):
        return mark_safe('<img src="{url}" width="300px" height="300px" />'.format(url=obj.logo.url))
    
@admin.register(models.Ami_user)
class Ami_userAdmin(admin.ModelAdmin):
    list_display = ('user_one','user_two','status','date_add','date_upd') 
    list_filter = ('status','date_add','date_upd')#les standard ou les foreignKey
    search_fields = ('user_one','user_two')#dois etre dans liste display; ne pas metres de stadard; prend le charField ou les relations 
    list_display_links = ('user_one','user_two')# tous les elements squf les standards
    list_per_page = 3
    ordering = ['user_one']
    date_hierarchy = 'date_add'
    # inlines = [SousCategorieInline]
    
    
    actions = ('active','deactive')
    
    def active(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,'la selections a été active avec seccès')
    active.short_description = 'active du groupe  sélectionée '
    
    def deactive(self,request,queryset):
        queryset.update(status=False)
        self.message_user(request,'la selections a ete désactive avec seccès')
    deactive.short_description = 'deactivé les groupe sélectionée '
    
@admin.register(models.MessageUser)
class MessageUserAdmin(admin.ModelAdmin):
    list_display = ('sender','salon','message','status','date_add','date_upd') 
    list_filter = ('status','date_add','date_upd')#les standard ou les foreignKey
    search_fields = ('sender','salon')#dois etre dans liste display; ne pas metres de stadard; prend le charField ou les relations 
    list_display_links = ('sender',)# tous les elements squf les standards
    # list_per_page = 3
    ordering = ['sender']
    date_hierarchy = 'date_add'
    # inlines = [SousCategorieInline]
    # readonly_fields=['detaile_image']
    
    actions = ('active','deactive')
    
    def active(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,'la selections a été active avec seccès')
    active.short_description = 'active du Message  sélectionée '
    
    def deactive(self,request,queryset):
        queryset.update(status=False)
        self.message_user(request,'la selections a ete désactive avec seccès')
    deactive.short_description = 'deactivé les Message sélectionée '
    
@admin.register(models.User_groupe)
class User_groupeAdmin(admin.ModelAdmin):
    list_display = ('groupe','user','is_admin','status','date_add','date_upd') 
    list_filter = ('status','date_add','date_upd')#les standard ou les foreignKey
    search_fields = ('sender','salon')#dois etre dans liste display; ne pas metres de stadard; prend le charField ou les relations 
    list_display_links = ('groupe','user')# tous les elements squf les standards
    # list_per_page = 3
    ordering = ['groupe']
    date_hierarchy = 'date_add'
    # inlines = [SousCategorieInline]
    # readonly_fields=['detaile_image']
    
    actions = ('active','deactive')
    
    def active(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,'la selections a été active avec seccès')
    active.short_description = 'active du Message  sélectionée '
    
    def deactive(self,request,queryset):
        queryset.update(status=False)
        self.message_user(request,'la selections a ete désactive avec seccès')
    deactive.short_description = 'deactivé les Message sélectionée '
    

@admin.register(models.Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = ('get_slog','nom','sender_one','sender_two','type','status','date_add','date_upd') 
    list_filter = ('status','date_add','date_upd')#les standard ou les foreignKey
    #search_fields = ()#dois etre dans liste display; ne pas metres de stadard; prend le charField ou les relations 
    #list_display_links = ()# tous les elements squf les standards
    # list_per_page = 3
    #ordering = ['nom']
    date_hierarchy = 'date_add'
    # inlines = [SousCategorieInline]
    # readonly_fields=['detaile_image']
    
    actions = ('active','deactive')
    
    def active(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,'la selections a été active avec seccès')
    active.short_description = 'active du Message  sélectionée '
    
    def deactive(self,request,queryset):
        queryset.update(status=False)
        self.message_user(request,'la selections a ete désactive avec seccès')
    deactive.short_description = 'deactivé les Message sélectionée '
