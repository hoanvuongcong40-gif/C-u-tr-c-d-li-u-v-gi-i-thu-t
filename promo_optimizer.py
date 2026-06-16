"""
promo_optimizer.py

Phần 3:
- Fibonacci (Tabulation)
- Climbing Stairs
- Knapsack 0/1 (2D)
- Trace Back
- Knapsack 0/1 (1D)
"""


# ==================================================
# FIBONACCI TABULATION
# ==================================================

def fib_tab(n):

    if n <= 1:
        return n

    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):

        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# ==================================================
# CLIMBING STAIRS
# ==================================================

def climb_stairs(n):

    if n == 0:
        return 1

    if n <= 2:
        return n

    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):

        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# ==================================================
# DEMO DP BASICS
# ==================================================

def demo_dp_basics():

    print("\n===== DYNAMIC PROGRAMMING =====")

    n = 7

    print(f"\nFibonacci({n}) = {fib_tab(n)}")

    print(
        f"So cach leo {n} bac = "
        f"{climb_stairs(n)}"
    )


# ==================================================
# KNAPSACK 2D
# ==================================================

def build_combo_dp_table(
        prices,
        scores,
        budget_limit):

    n = len(prices)

    dp = [
        [0] * (budget_limit + 1)
        for _ in range(n + 1)
    ]

    for i in range(1, n + 1):

        for budget in range(
                budget_limit + 1):

            dp[i][budget] = (
                dp[i - 1][budget]
            )

            if prices[i - 1] <= budget:

                dp[i][budget] = max(

                    dp[i][budget],

                    scores[i - 1]
                    +
                    dp[
                        i - 1
                    ][
                        budget
                        - prices[i - 1]
                    ]
                )

    return dp


# ==================================================
# TRACE BACK
# ==================================================

def trace_combo_from_dp(
        dp,
        prices,
        budget_limit):

    selected_items = []

    i = len(prices)

    budget = budget_limit

    while i > 0 and budget > 0:

        if dp[i][budget] != dp[i - 1][budget]:

            selected_items.append(
                i - 1
            )

            budget -= prices[i - 1]

        i -= 1

    selected_items.reverse()

    return selected_items


# ==================================================
# DEMO KNAPSACK 2D
# ==================================================

def demo_combo_knapsack_2d():

    print(
        "\n===== KNAPSACK 2D ====="
    )

    prices = [2, 3, 4, 5]

    scores = [3, 4, 5, 8]

    budget_limit = 8

    dp = build_combo_dp_table(
        prices,
        scores,
        budget_limit
    )

    selected_items = (
        trace_combo_from_dp(
            dp,
            prices,
            budget_limit
        )
    )

    max_score = dp[
        len(prices)
    ][budget_limit]

    print(
        "\nNgan sach:",
        budget_limit
    )

    print(
        "Diem toi da:",
        max_score
    )

    print(
        "\nSan pham duoc chon:"
    )

    for item in selected_items:

        print(
            f"\nSan pham {item}"
        )

        print(
            f"Gia: {prices[item]}"
        )

        print(
            f"Diem: {scores[item]}"
        )


# ==================================================
# KNAPSACK 1D
# ==================================================

def combo_knapsack_1d(
        prices,
        scores,
        budget_limit):

    dp = [0] * (
        budget_limit + 1
    )

    for i in range(len(prices)):

        for budget in range(
                budget_limit,
                prices[i] - 1,
                -1):

            dp[budget] = max(

                dp[budget],

                scores[i]
                +
                dp[
                    budget
                    - prices[i]
                ]
            )

    return dp[budget_limit]


# ==================================================
# DEMO KNAPSACK 1D
# ==================================================

def demo_combo_knapsack_1d():

    print(
        "\n===== KNAPSACK 1D ====="
    )

    prices = [2, 3, 4, 5]

    scores = [3, 4, 5, 8]

    budget_limit = 8

    result = combo_knapsack_1d(
        prices,
        scores,
        budget_limit
    )

    print(
        "\nNgan sach:",
        budget_limit
    )

    print(
        "Diem toi da:",
        result
    )

    print(
        "\nBan 1D toi uu bo nho."
    )