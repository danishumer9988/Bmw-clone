from django.db import models
from django.contrib.auth.models import User

class ContactMessage(models.Model):
    SUBJECT_CHOICES = [
        ('GENERAL', 'General Inquiry'),
        ('SALES', 'Sales Question'),
        ('SERVICE', 'Service & Maintenance'),
        ('PARTS', 'Parts & Accessories'),
        ('TEST_DRIVE', 'Test Drive Request'),
        ('OTHER', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.get_subject_display()} - {self.created_at.strftime('%Y-%m-%d')}"