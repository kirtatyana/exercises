# Сортировка вставками
def insertion_sorting(lst):
    for i in range(1, len(lst)):
        j = i
        while j>0 and lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j = j-1
    return lst
    
lst = [int(i) for i in input().split()]
print(insertion_sorting(lst))






# Сортировка слиянием с рекурсивным вызовом
# слияние двух отсортированных списков
def merge(a, b):
    lst = [] # итоговый массив
    #i, j = 0, 0 # индексы массивов
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            lst.append(a.pop(0))
        else:
            lst.append(b.pop(0))
    if len(a) > 0:
        lst.extend(a)
    if len(b) > 0:
        lst.extend(b)
    return lst
    
# рекурсивная функция
def merge_sort(lst):
    if len(lst) > 1:
        m = int(len(lst) / 2)
        return merge(merge_sort(lst[0:m]), merge_sort(lst[m:]))
    else:
        return lst
    
lst = [int(i) for i in input().split()]
print(merge_sort(lst))
