from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=20)
    content=models.CharField(max_length=20)
    # file_path=models.FilePathField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title


