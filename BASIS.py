# variables ######################################
print('@@@@@@ BASIS CONVERTOR @@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ (Basis1 -> Basis2)')
hexa = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
hex_a = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
medium = ''

# input ##########################################
n = int(input('#Basis 1: '))
m = int(input('#Basis 2: '))
if n == 16:
    print('Tip: Your Numbers Should Follow This Pattern\n1, 2, 3, 4, 5, 6, 7, 8, 9, A(10), B(11), C(12), D(13), E(14), F(15).\n')
raw = input('#Enter your number: ')
raw_list = list(raw)

# convert from n -> 10 ###########################
if n == 10:
    medium = int(raw)
else:
    medium = 0
    for i in range(len(raw_list)):
        temp = 0
        i2 = -i - 1
        if raw_list[i2] in hexa:
            temp = hexa[raw_list[i2]]
        else:
            temp = int(raw_list[i2])
        medium = medium + temp * (n**i)
print('#Converetd to BASIS(10)= ' + str(medium))

# convert from 10 -> m ###########################
result = ''
if m == 10:
    result = str(medium)
else:
    while True:
        tempo = int(medium / m)
        temp = str(medium % m)
        if temp in hex_a:
            temp = hex_a[temp] 
        result = str(temp) + result
        if tempo < m:
            if tempo in hex_a:
                tempo = hex_a[tempo]        
            result = str(tempo) + result
            break
        medium = tempo

# print result ###################################
print('#Converted to BASIS(' + str(m) + ')= ' + str(result))
print('\n\nTo be or not to be :o')
input()
