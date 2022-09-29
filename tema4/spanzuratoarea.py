my_list = ['mar', 'para', 'portocala', 'banana', 'caisa', 'piersica', 'struguri', 'rodie', 'zmeura', 'ananas']

import random

my_list = random.choice(my_list)
answer = '-' * len(my_list)

print(answer)

life_nr = 0
while life_nr < 3:
    n = input('Litera este: ')
    n = n.lower()
    if len(n) != 1:
        print('You should type one letter!')
        continue
    elif not n.isalpha():
        print('The character is not a letter!')
        continue
    else:
        if n not in my_list:
            life_nr = life_nr + 1
            if life_nr == 3:
                print('You lost. The word was', my_list)
                break
            else:
                print('You have just ' + str(3 - life_nr) + ' more attempts.')
                continue
        else:
            answer_n = list(answer)
            answer = ""
        for x in range(len(answer_n)):
            if n == my_list[x]:
                answer_n[x] = n
            answer += answer_n[x]
        print(answer)
        if answer.find('-') == -1:
            print('You won! The word was', answer)
            break
