from django.forms import ModelForm
from cnpj_field.models import MyModel


class CNPJFieldForm(ModelForm):
    class Meta:
        model = MyModel
        fields = ['cnpj']
