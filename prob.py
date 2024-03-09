def merge_sorted_lists(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    i = len1 - 1  # Индекс последнего элемента в первом списке
    j = len2 - 1  # Индекс последнего элемента во втором списке

    # Создаем пустой результирующий список
    res = []

    # Пока есть элементы в обоих списках
    while i >= 0 and j >= 0:
        # Сравниваем элементы
        if list1[i] >= list2[j]:
            res.append(list1[i])
            i -= 1
        else:
            res.append(list2[j])
            j -= 1

    # Добавляем оставшиеся элементы из первого списка (если есть)
    while i >= 0:
        res.append(list1[i])
        i -= 1

    # Добавляем оставшиеся элементы из второго списка (если есть)
    while j >= 0:
        res.append(list2[j])
        j -= 1

    return res


# Пример использования
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = merge_sorted_lists(a, b)
print(res) 

c1, b1 = map(int, input().split())
t = 0 # Время 
x = 0 # количество потухших бенгальских огней
while c1 >= b1:
    t += c1
    x += c1
    c1 = 2 * (x // b1)
    x %= b1
print(t)
# мы каждый раз исплоьзуем все огни и храним в x количество огней из которых мы можем сделать новые огни
