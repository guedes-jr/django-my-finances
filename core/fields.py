from django.db import models
from django.core.exceptions import ValidationError
import re

class MonthYearField(models.CharField):
    description = "Month and Year in YYYY-MM format"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 7  # YYYY-MM format
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        if isinstance(value, str):
            return value
        return super().to_python(value)

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        if not re.match(r'^\d{4}-(0[1-9]|1[0-2])$', value):
            raise ValidationError("This field must be in YYYY-MM format.")
