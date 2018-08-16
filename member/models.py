from django.db import models

# Create your models here.
class Member(models.Model):
    UserName = models.CharField(max_length=20,null=False)
    UserEmail = models.EmailField(max_length=100,null=False)
    UserPassword = models.CharField(max_length=20,null=False)
    BabyName = models.CharField(max_length=20,null=False)
    
    # class Meta:
    #     db_table = "member"
