from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from private_storage.fields import PrivateFileField

from core.models import BaseModel
from core.constants import (ALLOWED_IMAGE_MIME_TYPES, MAX_IMAGE_FILE_SIZE)
from . import constants


class Recipe(BaseModel):
    pass
