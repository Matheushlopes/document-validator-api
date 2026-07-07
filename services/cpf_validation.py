from functools import reduce

def limpar_cpf(cpf):
    return "".join(filter(str.isdigit, cpf))


def calcular_digito(digitos, contador):
    resultados = []

    for digito in digitos:
        resultados.append(int(digito) * contador)
        contador -= 1

    soma = reduce(lambda a, b: a + b, resultados)
    resto = soma % 11

    if resto <= 1:
        return "0"

    return str(11 - resto)


def validar_cpf(cpf):
    cpf = limpar_cpf(cpf)

    if len(cpf) != 11:
        return "Digite CPF com 11 Digitos"

    if cpf == cpf[0] * 11:
        return False

    nove_digitos = list(cpf[:9])

    primeiro_digito = calcular_digito(nove_digitos, 10)
    nove_digitos.append(primeiro_digito)

    segundo_digito = calcular_digito(nove_digitos, 11)
    nove_digitos.append(segundo_digito)

    cpf_calculado = "".join(nove_digitos)

    return ({
        "cpf":cpf_calculado,
        "valido":cpf == cpf_calculado,
    })