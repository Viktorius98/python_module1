def __iter__(self): # объявляем класс как итератор
    self.current = self.first # в текущий элемент помещаем первый
    return self # возвращаем итератор

def __next__(self): # метод перехода
    if self.current is None: # если текущий стал последним
        raise StopIteration # вызываем исключение
    else:
        node = self.current # сохраняем текущий элемент
        self.current = self.current.next # совершаем переход
        return node # и возвращаем сохраненный
def __len__(self):
    count = 0
    pointer = self.first
    while pointer is not None:
        count += 1
        pointer = pointer.next
    return count
