def generate_square(n):
    row = "*" * n
    return [row for _ in range(n)]
print(generate_square(4))