from django.db import models
from django.contrib.auth.models import User
# table name  - todo
        # column - title(length-100,string),
        # description(length-unlimited,string), status(bool)
        
class Todo(models.Model):
    # class variable
    # char = string
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    # Workout
    # I will be doing 2 hours of workout for a week
    # false
    
    
    


