""""
PRIMEIRA VERSÃO DO VALIDATOR CPF
APÓS CRIADO, FUI REFATORANDO E APLICANDO NOVOS CONCEITOS APRENDIDOS
COMO reduce(lambda a, b: a + b, resultados), filte,map.
"""
from functools import reduce

cpf = "09584479938"

nine_digit = list(cpf[:-2])
two_digit = list(cpf[-2::])

def calc_cpf(contador,result = None):
    if isinstance(result, list):
        for indice in nine_digit:
            res = int(indice) * contador
            contador -= 1
            result.append(res)

    soma = reduce(lambda a, b: a + b, result)
    resultado_resto = soma % 11
    return resultado_resto

def verificador_digits(digits):
    if digits <= 1:
        j = 0
        nine_digit.append(str(j))
    elif digits <= 10:
        j = 11 - digits
        nine_digit.append(str(j))


def validator(cpf,cpf_final):
    if cpf == cpf_final:
        return True
    else:
        return False

verificador_digits(calc_cpf(10,[]))
verificador_digits(calc_cpf(11,[]))
cpf_final = "".join(nine_digit)

print(cpf_final)

print(validator(cpf,cpf_final))
