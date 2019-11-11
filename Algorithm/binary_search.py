# put your python code here
# lst - список, в котором необходимо найти элемент el
# возвращает индекс элемента, или -1, если такого элемента не найдено
def find_x (lst, el):
    bg, ed = 0, len(lst)-1 # индексы начало и конца поиска
    ind = 0 # искомый индекс
    while bg <= ed and ind <= len(lst)-1:
        ind = int((bg + ed)/2)
        if lst[ind] == el:
            return ind+1
        elif lst[ind] > el:
            ed = ind - 1
        else:
            bg = ind + 1
    return -1
