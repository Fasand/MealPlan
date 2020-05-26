from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from ordered_model.models import OrderedModel

from .managers import (BaseManager, OrderedBaseManager)


class BaseModel(models.Model):
    active = models.BooleanField(_('active'), default=True)

    created = models.DateTimeField(
        _('datetime created'), default=timezone.now, editable=False)
    modified = models.DateTimeField(
        _('datetime modified'), default=timezone.now)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True,
                                   related_name='created_%(class)s_objects',
                                   on_delete=models.SET_NULL,
                                   verbose_name=_('created by'))
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    null=True, blank=True,
                                    related_name='modified_%(class)s_objects',
                                    on_delete=models.SET_NULL,
                                    verbose_name=_('modified by'))

    objects = BaseManager()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.pk:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(BaseModel, self).save(*args, **kwargs)

    def activate(self):
        self.active = True
        self.save()

    def deactivate(self):
        self.active = False
        self.save()

    class Meta:
        abstract = True
        ordering = ('-active', '-modified')


class OrderedBaseModel(BaseModel, OrderedModel):
    objects = OrderedBaseManager()

    class Meta(OrderedModel.Meta):
        abstract = True


class User(AbstractUser):
    pass
