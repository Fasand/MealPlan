from django.utils.translation import ugettext_lazy as _

UNIT_TYPE_WEIGHT = 'weight'
UNIT_TYPE_VOLUME = 'volume'

UNIT_TYPES = (
    (UNIT_TYPE_WEIGHT, _('unit weight')),
    (UNIT_TYPE_VOLUME, _('unit volume')),
)

UNIT_SYSTEM_CUSTOM = 'custom'
UNIT_SYSTEM_METRIC = 'metric'
UNIT_SYSTEM_IMPERIAL_UK = 'imperial_uk'
UNIT_SYSTEM_IMPERIAL_US = 'imperial_us'

UNIT_SYSTEMS = (
    (UNIT_SYSTEM_CUSTOM, _('unit custom')),
    (UNIT_SYSTEM_METRIC, _('unit metric')),
    (UNIT_SYSTEM_IMPERIAL_UK, _('unit imperial uk')),
    (UNIT_SYSTEM_IMPERIAL_US, _('unit imperial us')),
)
