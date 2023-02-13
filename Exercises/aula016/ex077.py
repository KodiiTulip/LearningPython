words = ('APRENDER',
         'PYTHON',
         'LINGUAGEM',
         'GRATIS',
         'CURSO',
         'VIDEO',
         'DERIVAKAT',
         'ANY',
         'SECOND',
         'MINUTE',
         'STAY',
         'DAWN',
         'LIVE',
         'FIVE',
         'EYES',
         'SLEEP',
         'DEJAVU')
for word in words:
    print(f'\n[@] A palavra "{word}" tem as vogais ', end='')
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f'{letter.upper()}', end=' ')
