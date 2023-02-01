people = []
for i in range(0, 2):
    name = input(f'[@] What name? ')
    age = input(f'[@] What age? ')
    gender = input(f'[@] What gender?')
    people.insert(i, dict(name=name, age=age, gender=gender))

for o in range(0, len(people)):
    print(people[o])
for n in range(0, len(people)):
    if people[n]['gender'] in 'm':
        print(True)
    else:
        print(False)
