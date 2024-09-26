#função trunc transforma numero real/decimal em sua versão inteira
from math import trunc
num = float(input('Digite um valor: '))
print(f"O valor digitado foi {num} e a sua porção inteira é {trunc(num)}")