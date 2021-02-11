import re
from django.core.exceptions import ValidationError

INVALIDS_CNPJ = ("00000000000000", "11111111111111", "22222222222222", "33333333333333", "44444444444444",
                 "55555555555555", "66666666666666", "77777777777777", "88888888888888", "99999999999999")


def digit_verify(value: str, second=False):
    """Valida combinação de números como CNPJ válido e possível de existir com base nos dois últimos dígitos"""
    array_weight = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6]  # Array de peso para o reverso de cada postion(lê-se [::-1])
    sum_digit = 0  # Somatoria de digitos
    gen_range = 12  # Verifica primeiros 12 caracteres

    if second is True:  # IF para manutenção do código em caso de segundo dígito verificador a ser analisado
        gen_range += 1  # Verifica primeiros 13 caracteres
        cnpj = (str(value[::-1]))[1:]
    else:
        cnpj = (str(value[::-1]))[2:]

    for n in range(0, gen_range):
        sum_digit += int(int(cnpj[n]) * array_weight[n])  # calcula o peso de cada caractere pelo weight

    digit = sum_digit % 11

    if digit < 2:
        digit = 0
    else:
        digit = 11 - digit

    return digit


def validate_cnpj(value):
    # Extract numbers from string
    cnpj = re.sub('[^0-9]', "", value)
    if len(cnpj) != 14:
        raise ValidationError('CNPJ deve conter 14 números', 'invalid')

    # Calculate first validator digit from string
    first_digit = digit_verify(cnpj)

    # Calculate second validator digit from string
    second_digit = digit_verify(cnpj, second=True)

    # Checks whether the cpf is on the list of invalid persons or if a check digit does not match the digits calculated
    # in the expression
    if cnpj in INVALIDS_CNPJ or (not cnpj[-2:] == "%s%s" % (first_digit, second_digit)):
        raise ValidationError('Número de CNPJ inválido', 'invalid')
    return "CERTO"