from django.utils.translation import ugettext_lazy as _

DIFFICULTY_V_EASY = 1
DIFFICULTY_EASY = 2
DIFFICULTY_MEDIUM = 3
DIFFICULTY_HARD = 4
DIFFICULTY_V_HARD = 5


DIFFICULTIES = (
    (DIFFICULTY_V_EASY, _('very easy')),
    (DIFFICULTY_EASY, _('easy')),
    (DIFFICULTY_MEDIUM, _('medium')),
    (DIFFICULTY_HARD, _('hard')),
    (DIFFICULTY_V_HARD, _('very hard')),
)

DURATION_PREP = 'prep'
DURATION_COOK_ACTIVE = 'cook active'
DURATION_COOK_PASSIVE = 'cook passive'

DURATION_TYPES = (
    (DURATION_PREP, _('prep')),
    (DURATION_COOK_ACTIVE, _('cook (active)')),
    (DURATION_COOK_PASSIVE, _('cook (unattended)')),
)
