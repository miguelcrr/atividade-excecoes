class NumeroImparError(Exception):
    pass
try:
    x=int(input('Digite um numero inteiro e par:'))
    if x % 2 == 1:
        raise NumeroImparError(x)
    print("O numero digitado e par")
except NumeroImparError as e:
    print("Erro! O numero digitado e impar")
