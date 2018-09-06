from django.db import models

class User(models.Model):
    first =models.CharField(max_length=255) 
    last =models.CharField(max_length=255)
    email =models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"[Object for {self.first}]"

