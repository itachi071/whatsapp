from django.db import models

class Upload_Data(models.Model):
    Name = models.CharField(max_length=50)
    File = models.FileField(upload_to='files/',default='Na')
  

 