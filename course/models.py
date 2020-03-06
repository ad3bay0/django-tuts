from django.db import models
import uuid

STATUS = (
    ('ACTIVE','ACTIVE'),
    ('INACTIVE','INACTIVE')
)

# Create your models here.
class Course(models.Model):
     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     name = models.CharField(max_length=100)
     choice = models.CharField(max_length=255, default='ACTIVE',choices=STATUS)
        