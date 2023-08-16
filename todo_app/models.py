from django.db import models

# table name  - todo
        # column - title(length-100,string),
        # description(length-unlimited,string), status(bool)
        
class Todo(models.Model):
    # class variable
    # char = string
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False)
    
    # Workout
    # I will be doing 2 hours of workout for a week
    # false
    
    
    


