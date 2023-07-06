from django.db import models

# Create your models here.
class Images(models.Model):
    image = models.FileField(upload_to='images',blank=True, null=True)
    
    def __str__(self):
        return str(self.image)