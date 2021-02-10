from django.db import models

from .validators import validate_cnpj


class CNPJField(models.CharField):
    default_validators = [validate_cnpj]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 14)
        super().__init__(*args, **kwargs)


class MyModel(models.Model):
    cnpj = CNPJField('CNPJ')
