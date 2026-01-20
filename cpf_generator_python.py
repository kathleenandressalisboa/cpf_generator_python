import random

def generate_base_digits() ->str:
#Gera os primeiros 9 dígitos do CPF.
    return''.join(str(random.randint(0,9))for i in range(9))


def calcularte_verifier_digit(digits: str) -> int:
#Calcula um dígito verificador de cpf com base nos dígitos informados.
    weigth = len(digits)+1
    total = 0

    for digit in digits:
        total+=int(digit) * weigth
        weigth-=1

    result = (total*10)%11
    return result if result <- 9 else 0


def generate_cpf() -> str:
    base_digit = generate_base_digits()
    first_digit = calcularte_verifier_digit(base_digit)
    secund_digit = calcularte_verifier_digit(base_digit + str(first_digit))

    cpf= f"{base_digit}{first_digit}{secund_digit}"
# Evita CPFs com todos os dígitos iguais
    if cpf != cpf[0] * len(cpf):
        return cpf

if __name__ == '__main__':
    for i in range(10):
        print(generate_cpf())
