# Кейс-задача № 4
# Максимальная сила стаи при суммарном числе голов N.
# Один дракон может иметь от 1 до 7 голов.

def max_strength(n):
    # dp[s] — максимальная сила для суммы s.
    dp = [0] * (n + 1)
    dp[0] = 1

    for s in range(1, n + 1):
        best = 0
        for heads in range(1, 8):
            if heads <= s:
                best = max(best, dp[s - heads] * heads)
        dp[s] = best

    return dp[n]


if __name__ == "__main__":
    n = int(input())
    if not (0 < n < 100):
        raise ValueError("N должно удовлетворять условию 0 < N < 100")

    print(max_strength(n))
