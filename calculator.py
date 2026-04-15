def sum_even_numbers(n):
    total = 0
    for i in range(1, n + 1):   # vòng lặp
        if i % 2 == 0:          # rẽ nhánh
            total += i
    return total


if __name__ == "__main__":
    print(sum_even_numbers(5))