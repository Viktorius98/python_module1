arroy = list(map(int, input('Введите любую последовательность чисел через пробел: ').split()))
some_number = int(input('Введите любое число: '))

while some_number:
    if some_number <= min(arroy):
        print('Введенное число не соответствует критериям поиска, введите число не превышающее максимальное значение и'
              'больше минимального')
        some_number = int(input('Введите любое число: '))
    elif some_number > max(arroy):
        print('Введенное число не соответствует критериям поиска, введите число не превышающее максимальное значение и'
              'больше минимального')
        some_number = int(input('Введите любое число: '))
    else:
        break

def buble(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

array_1 = buble(array)

def binary_search(array_1, some_number, left, right):

    if left > right:
        return False
    middle = (right + left) // 2
    if array_1[middle] < some_number and array_1[middle + 1] >= some_number:
        return middle
    elif some_number < array_1[middle]:
        return binary_search(array_1, some_number, left, middle -1)
    else:
        return binary_search(array_1, some_number, middle + 1, right)

print(binary_search(array_1, some_number, 0, len(array_1) - 1))
