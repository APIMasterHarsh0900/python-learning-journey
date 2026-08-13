def selection_sort(lst):
    n = len(lst)

    for passes in range(n - 1):
        min_index = passes

        for j in range(passes + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j

        lst[passes], lst[min_index] = lst[min_index], lst[passes]

    return lst
print(selection_sort([64, 25, 12, 22, 11]))