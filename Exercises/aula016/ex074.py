import random

num = (random.randint(0, 100),
       random.randint(0, 100),
       random.randint(0, 100),
       random.randint(0, 100),
       random.randint(0, 100))

print(f'[@] Números aleatóriamente gerados:')
print(f'[@] {num}')
print(f'[@] Maior número: {max(num)}\n'
      f'[@] Menor número: {min(num)}')
