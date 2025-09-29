class DivisaoPorZero(Exception):
    pass
try:
    numero=int(input("Digite um numero inteiro: "))
    if numero == 0:
        raise DivisaoPorZero()
    inteiro = int(numero)
    divisao = 10/numero
    print("Resultado da divisao:",divisao)
except DivisaoPorZero:
    print("Erro! O numero digitado e 0.")
except ValueError:
    print("Erro! O numero digitado nao e inteiro.")
