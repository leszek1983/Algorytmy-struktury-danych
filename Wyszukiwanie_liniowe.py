
lista = [33, 16, -1, 44, 7, 888, 0, 27, 69, 99, 174, 555, 81, 275, -50, 777]

print('Numery na liście: ', lista)

searchItem = int(input('Wprowadz numer ktorego szukasz: '))
found = False

for i in range(len(lista)):

    if lista[i] == searchItem:
        found = True
        print(searchItem, 'znajduje sie na pozycji nr', i)
        break

if found == False:
    print(searchItem, 'nie znajduje sie na liscie!')