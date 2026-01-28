import random

from selenium.webdriver.common.devtools.v140.fetch import continue_request


def generate_base_digits() ->str:
#Gera os primeiros 9 dígitos do CPF.
    return''.join(str(random.randint(0,9))for _ in range(9))


def calculate_verifier_digits(digits: str) -> int:
#Calcula um dígito verificador de cpf com base nos dígitos informados.
    weigth = len(digits)+1
    total = 0

    for digit in digits:
        total+=int(digit) * weigth
        weigth-=1

    result = (total*10)%11
    return result if result <= 9 else 0

def generate_cpf() ->str | None:
    #Gera um CPF válido para fins de teste.
    while True:
        base_digits: str = generate_base_digits()

        #Evita CPFs com todos os digítos iguais.
        if len(set(base_digits)) == 1:
            continue

        first_digit = calculate_verifier_digits(base_digits)
        secund_digit = calculate_verifier_digits(base_digits + str(first_digit))

        cpf= f"{base_digits}{first_digit}{secund_digit}"
        return cpf

if __name__ == '__main__':
    for i in range(10):
        print(generate_cpf())
