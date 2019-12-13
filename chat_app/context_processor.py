from . import  models as config 

def get_groupe(request):
    data={
    'allGroupe': config.GroupeChat.objects.filter(status=True),
        
    }
    
    return data
    