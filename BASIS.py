# variables ######################################
print('@@@@@@ BASIS CONVERTOR @@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ (Basis1 -> Basis2)')
hexa = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
hex_a = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
stepA = ''

# input ##########################################
n = int(input('#Basis 1: '))
m = int(input('#Basis 2: '))
if n == 16:
    print('Tip: Your Numbers Should Follow This Pattern\n1, 2, 3, 4, 5, 6, 7, 8, 9, A(10), B(11), C(12), D(13), E(14), F(15).\n')
N = input('#Enter your number: ')
N_list = list(N)

# convert from n -> 10 ###########################
if n == 10:
    stepA = int(N)
else:
    stepA = 0
    for i in range(len(N_list)):
        temp = 0
        i2 = -i - 1
        if N_list[i2] in hexa:
            temp = hexa[N_list[i2]]
        else:
            temp = int(N_list[i2])
        stepA = stepA + temp * (n**i)
print('#Converetd to BASIS(10)= ' + str(stepA))

# convert from 10 -> m ###########################
stepB = ''
if m == 10:
    stepB = str(stepA)
else:
    while True:
        tempo = int(stepA / m)
        temp = str(stepA % m)
        if temp in hex_a:
            temp = hex_a[temp] 
        stepB = str(temp) + stepB
        if tempo < m:
            if tempo in hex_a:
                tempo = hex_a[tempo]        
            stepB = str(tempo) + stepB
            break
        stepA = tempo

# print result ###################################
print('#Converted to BASIS(' + str(m) + ')= ' + str(stepB))
print('\n\nTo be or not to be :o')
input()
