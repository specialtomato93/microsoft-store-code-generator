from random import choice
chars = 'BCDFGHJKMNPQRTVWXYZ2346789'
with open('output.txt', 'a') as file:
    for _ in range(5000):
        file.write('-'.join(''.join(choice(chars) for _ in range(5)) for _ in range(5)) + '\n')