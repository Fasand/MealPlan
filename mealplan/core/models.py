from django.db import models


class BaseModel(models.Model):
    pass

    class Meta():
        abstract = True
