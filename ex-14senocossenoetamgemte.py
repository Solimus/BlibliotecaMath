import math
angulo =float(input('Digite o ângulo que você deseja:'))

seno = math.sin(math.radians(angulo)) #math.sin calcula o seno
print(f"O ângulo de {angulo} tem o SENO de {seno:.2f}")

cosseno = math.cos(math.radians(angulo))#math.cos calcula o cosseno
print(f"o ângulo de {angulo}tem o COSSENO de {cosseno:.2f}")

tangente = math.tan(math.radians(angulo))#math.tan calcula o tangente
print(f"O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}")