from django.db import models

from private_storage.fields import PrivateFileField
from core.constants import (ALLOWED_IMAGE_MIME_TYPES, MAX_IMAGE_FILE_SIZE)


class PrivateImageField(PrivateFileField):
    def __init__(self, *args, **kwargs):
        # Content types always stay the same
        kwargs['content_types'] = ALLOWED_IMAGE_MIME_TYPES
        # Max File Size can be changed in the constructor
        kwargs['max_file_size'] = kwargs.pop(
            'max_file_size', None) or MAX_IMAGE_FILE_SIZE
        super().__init__(*args, **kwargs)


    # TODO: Clean the file properly, using Pillow or similar
    # from django.core.files.uploadedfile import UploadedFile
    # from django.core.exceptions import ValidationError
    # from django.template.defaultfilters import filesizeformat
    # def clean(self, *args, **kwargs):
    #     data = super(PrivateFileField, self).clean(*args, **kwargs)
    #     file = data.file
    #     if isinstance(file, UploadedFile):
    #         # content_type is only available for uploaded files,
    #         # and not for files which are already stored in the model.
    #         content_type = file.content_type

    #         if self.content_types and content_type not in self.content_types:
    #             # logger.debug('Rejected uploaded file type: %s', content_type)
    #             raise ValidationError(self.error_messages['invalid_file_type'])

    #         if self.max_file_size and file.size > self.max_file_size:
    #             raise ValidationError(self.error_messages['file_too_large'].format(
    #                 max_size=filesizeformat(self.max_file_size),
    #                 size=filesizeformat(file.size)
    #             ))

    #     return data
