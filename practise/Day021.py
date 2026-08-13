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

def count_negatives(grid):
    count = 0

    for row in grid:
        left = 0
        right = len(row) - 1
        first_negative = len(row)

        while left <= right:
            mid = (left + right) // 2

            if row[mid] < 0:
                first_negative = mid
                right = mid - 1
            else:
                left = mid + 1

        count += len(row) - first_negative

    return count
print(count_negatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))