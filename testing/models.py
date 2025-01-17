from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200, default=None, blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return f'{self.name} - {self.subject}'
    
class Newsletter(models.Model):
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.email