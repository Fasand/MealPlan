from django.db import models
from ordered_model.models import OrderedModelManager


class BaseManager(models.Manager):
    pass


class OrderedBaseManager(BaseManager, OrderedModelManager):
    pass
