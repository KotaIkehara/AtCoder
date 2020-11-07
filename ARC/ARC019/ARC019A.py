S = input()

for game, real in zip('ODIZSB', '001258'):
    S = S.replace(game, real)
print(S)
