from django.db import models

class movies(models.Model):
    name=models.CharField(max_length=100,null=True)
    year=models.CharField(max_length=100,null=True)
    rating=models.CharField(max_length=100,null=True)
    img_url=models.CharField(max_length=100,null=True)

    def __str__(self):
       return self.name

class tv(models.Model):
    name=models.CharField(max_length=100,null=True)
    year=models.CharField(max_length=100,null=True)
    rating=models.CharField(max_length=100,null=True)
    img_url=models.CharField(max_length=100,null=True)

    def __str__(self):
       return self.name
