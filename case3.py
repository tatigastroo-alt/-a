# Кейс-задача № 3
# Найти сумму отрицательных элементов, расположенных
# между максимальным и минимальным элементами массива.

def solve(a):
    if not a:
        return 0

    max_pos = a.index(max(a))
    min_pos = a.index(min(a))

    left = min(max_pos, min_pos)
    right = max(max_pos, min_pos)

    return sum(x for x in a[left + 1:right] if x < 0)


if __name__ == "__main__":
    # Ввод: N, затем N целых чисел.
    n = int(input())
    a = list(map(int, input().split()))

    if len(a) != n:
        raise ValueError("Количество элементов массива не совпадает с N")

    print(solve(a))
