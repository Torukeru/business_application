from django.db import models

# Create your models here.
class Stall(models.Model):
    stall_id = models.BigAutoField(primary_key=True, blank=False)
    stall_type = models.CharField(max_length=55, blank=False)
    stall_location= models.CharField(max_length=55, blank=False, default='null')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'stall'
    
    def __str__(self):
        return self.stall_type

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True, blank=False)
    first_name = models.CharField(max_length=55, blank=False)
    middle_name = models.CharField(max_length=55, blank =True)
    last_name = models.CharField(max_length=55, blank=False)
    stall_name = models.CharField(max_length=55, blank=False, default='null')
    age = models.IntegerField(blank=False)
    birth_date = models.DateField(blank=False)
    stall = models.ForeignKey(Stall, on_delete=models.CASCADE)
    gender = models.CharField(max_length=55, blank=False)
    username = models.CharField(max_length=55, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    

    class Meta:
        db_table = 'users'