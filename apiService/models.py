from django.db import models
#from django.utils.translation import ugettext_lazy as _

# Create your models here.

#class User(models.Model):
 #   USER_TYPES = (
   #    ("Admin", "Admin"),
  #     ("SuperAdmin", "SuperAdmin"),
    #   ("Org", "Org")
   ###username = models.CharField(max_length=255,null=False)
    #is_staff = models.BooleanField(_("staff status"), default=False)
    #s_active = models.BooleanField(_("active status"), default=True)
    #user_type = models.CharField(max_length=255,choices=USER_TYPES)
    
    #def __str__(self):
    #    return self.username

class Songs(models.Model): 
    #user = user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=255,null =False)
    artist = models.CharField(max_length=255, null=False)
    #owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    def __str__(self):
        return "Song:{}  Artist:{}".format(self.title,self.artist)



