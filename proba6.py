def binary_search(array_1, some_number, left, right):

    if left > right:
        return False

    middle = (right+left) // 2
    if array_1[middle] < some_number and array_1[middle + 1] >= some_number:
        return middle
    elif some_number < array_1[middle]:
        return binary_search(array_1, some_number, left, middle-1)
    else:
        return binary_search(array_1, some_number, middle+1, right)

some_number = int(input())
array_1 = [i for i in range(0, len(array_1)-1)]

print(binary_search(array_1, some_number, 0, len(array_1) - 1))




some_number = int(input())
array_1 = [i for i in range(0, len(array_1)-1)]