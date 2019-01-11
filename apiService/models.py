from django.db import models


#Songs Api Model
class Songs(models.Model): 

    title = models.CharField(max_length=255,null =False)
    artist = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "Song:{}  Artist:{}".format(self.title,self.artist)



