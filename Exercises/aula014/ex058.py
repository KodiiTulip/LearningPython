import random
from Libraries.numeric_check import isint

rnum1 = random.randint(0, 10)

print(f'[@] Eu estou pensando em um número entre 1 e 10...')
print(f'[@] Você consegue adivinhar? Aqui estão algumas opções para te ajudar!')
tries = 1
while True:
    while True:
        answer = input(f'>>> ')
        if isint(answer):
            answer = int(answer)
            if 11 > answer > -1:
                break
            else:
                print(f'[@] \033[1;31m"{answer}" não está entre 0  e 10.\033[m')
        else:
            print(f'[@] \033[1;31m"{answer}" não é válido!\033[m')

    if answer == rnum1:
        print(f'[@] PARBÉNS!!! O número que eu estava pensando era {answer}!!\n'
              f'[@] Você usou {tries} tentativas para conseguir!!')
        break
    else:
        print(f'[@] Desculpe anjinho mas {answer} não era o número escolhido, tente de novo.')
        tries += 1
    if tries > 6:
        print(f'[@] Uma dica: o número está entre {rnum1 - 3} e {rnum1 + 2}')
    if tries > 10:
        print(f'[@] Desculpe anjinho mas você tentou mais de 10 vezes e não conseguiu.')
