'''
from common.models import DataTransferObject
from django.db import models
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_prj.settings")

class CrimeVO(models.Model):
    police = models.TextField()
    crime = models.TextField()
    create_at = models.DateTimeField()


class CrimeDTO(DataTransferObject):
    police = ''
    crime = ''
    create_at = ''
'''