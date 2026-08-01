def lift_rounds(n, capacity):
    rounds = n // capacity

    if n % capacity != 0:
        rounds += 1

    return rounds
print(lift_rounds(10, 3))