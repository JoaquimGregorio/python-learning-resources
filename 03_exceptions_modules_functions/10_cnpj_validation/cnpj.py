from re import sub
from random import randint


def format_cnpj(cnpj: str):
    return sub(r"[^0-9]", "", cnpj)


def is_sequence(cnpj: str):
    return cnpj == cnpj[0] * len(cnpj)


def get_digit(partial_cnpj: str):
    multipliers = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    start = len(multipliers) - len(partial_cnpj)
    multipliers = multipliers[start:]
    total = sum([int(x) * y for x, y in zip(partial_cnpj, multipliers)])
    digit = 11 - (total % 11)
    digit = digit if digit < 10 else 0
    return digit


def validate(cnpj: str):
    try:
        cnpj = format_cnpj(cnpj)
        if is_sequence(cnpj):
            return False
        new_cnpj = cnpj[:-2]
        new_cnpj += str(get_digit(new_cnpj))
        new_cnpj += str(get_digit(new_cnpj))

        return new_cnpj == cnpj
    except:
        return False


def reformat_cnpj(cnpj: str):
    cnpj = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
    return cnpj


def generate_cnpj(formated: bool = False):
    partial_cnpj = str(randint(10000000, 99999999))
    while is_sequence(partial_cnpj):
        partial_cnpj = str(randint(10000000, 99999999))
    partial_cnpj += "0001"
    partial_cnpj += str(get_digit(partial_cnpj))
    cnpj = partial_cnpj + str(get_digit(partial_cnpj))

    if formated:
        return reformat_cnpj(cnpj)
    return cnpj
