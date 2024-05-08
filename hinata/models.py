from django.db import models

# Create your models here.
#user model 
class TdListName(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name
    

#todo class
class Todomodel(models.Model):
    user = models.ForeignKey(TdListName, on_delete = models.CASCADE)
    task_name = models.CharField(max_length =200)
    complete = models.BooleanField(default=False)
    


    

#class for leaderbord
class LeaderBoard(models.Model):
    leaderUser = models.ForeignKey(TdListName, on_delete = models.CASCADE)
    user_score = models.IntegerField()
