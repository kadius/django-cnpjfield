# CNPJField (pt-br)
Campo validador de **CNPJ** para django>3.0
1. **Não valida perante a RFB.**
2. Válida independente da máscara aplicada
3. Não salva com máscara no banco de dados

## Como instalar:
### PIP
	pip install django-cnpjfield
### Django settings
	INSTALLED_APPS = [
    ...
    'cnpj_field',
    ]
### Model django
É permitido **incluir** argumentos regulares *(blank, null, e etc)* de **Fields** no **CNPJField**.

	from django.db import models
	from cnpj_field.models import CNPJField
	
	class MyModel(models.Model):
		...
		cnpj = CNPJField()
***
### Requisitos
1. Django>=3.0
2. Python 3.8
***
#### CNPJ inválido e válido
CNPJ inválido e todo e qualquer CNPJ que não contiver dígitos verificadores válidos ou não tenha o tamanho de um CNPJ (`max_lenght = 14`).

CNPJ válido é todo aquele que conter os dois últimos dígitos verificadores confirmados e possuir tamanho de 14 caracteres. 
**O ALGORITMO NÃO VÁLIDA PERANTE A RECEITA FEDERAL**

***
#### Agradecimentos
Agradeço ao [gabrielloliveira](https://pypi.org/user/gabrielloliveira/) por disponibilizar o seu CPFField, cujo qual utilizei como base na criação desse algoritmo.