from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_days(value):
    if (value not in [30,60,90]):
        raise ValidationError(
            _('Number of days must be 30, 60 or 90 days!'),
            params={'value': value},
        )