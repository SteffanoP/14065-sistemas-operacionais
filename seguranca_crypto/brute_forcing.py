from time import time

time_start = time()
your_list = 'tes'
complete_list = []
for current in range(5):
    a = list(your_list)
    for y in range(current):
        a = [x+i for i in your_list for x in a]

    complete_list = complete_list+a

for word, pos in zip(complete_list, range(100000)):
    if word == 'test':
        print('A senha é: '+word)
        print('Posição: '+ str(pos))
        break

print('Tempo de execução: '+str(time()-time_start))