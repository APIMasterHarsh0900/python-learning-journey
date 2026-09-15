def count_to_n(n):
    if n <= 0:
        return []

    result = count_to_n(n - 1)
    result.append(n)

    return result
print((count_to_n(5)))