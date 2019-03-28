from django.db import models

class moviesandtv(models.Model):
    name=models.CharField(max_length=100,null=True)
    year=models.DecimalField(max_digits=4,decimal_places=0,null=True)
    rating=models.DecimalField(max_digits=3,decimal_places=1,null=True)
    img_url=models.CharField(max_length=100,null=True)

    def __str__(self):
       return self.name
