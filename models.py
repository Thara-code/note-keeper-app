from django.db import models

# Create your models here.

class Notes(models.Model):
  Notes_Title = models.CharField(max_length=30)
  Notes_Desc = models.TextField()
  time = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.Notes_Title