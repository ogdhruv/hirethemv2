from django.utils.deconstruct import deconstructible
from django.core import validators
from django.utils.translation import gettext_lazy as _


# resume pdf validator (NOT IN USE)
def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension, only pdf is supported.')


# instagram like username validator (NOT IN USE)
@deconstructible
class CustomUnicodeUsernameValidator(validators.RegexValidator):
    regex = r"^(?!.*\.\.)(?!.*\.$)[^\W][\w.]{0,29}$"
    message = _(
        "Enter a valid username. This value may contain only letters, "
        "numbers, no spaces and ./_ characters."
        "username cannot start with a period."
    )
    flags = 0