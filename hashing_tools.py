"""
hashing_tools.py

Phần 2:
- OrderHashTable
- Group Anagrams
- Longest Consecutive Sequence
- Subarray Sum = K
- Rolling Hash (Rabin-Karp)
"""

from collections import defaultdict


# ==================================================
# ORDER HASH TABLE
# ==================================================

class OrderHashTable:

    def __init__(self, size=10):

        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, order_id):

        return hash(order_id) % self.size

    def insert(self, order_id, order_data):

        index = self._hash(order_id)

        bucket = self.table[index]

        for i, (key, value) in enumerate(bucket):

            if key == order_id:

                bucket[i] = (
                    order_id,
                    order_data
                )

                return

        bucket.append(
            (
                order_id,
                order_data
            )
        )

    def get(self, order_id):

        index = self._hash(order_id)

        bucket = self.table[index]

        for key, value in bucket:

            if key == order_id:
                return value

        return None

    def remove(self, order_id):

        index = self._hash(order_id)

        bucket = self.table[index]

        for i, (key, value) in enumerate(bucket):

            if key == order_id:

                del bucket[i]

                return True

        return False


# ==================================================
# DEMO HASH TABLE
# ==================================================

def demo_order_hash_table():

    print("\n===== ORDER HASH TABLE =====")

    orders = OrderHashTable()

    orders.insert(
        "ORD001",
        {
            "customer": "Nam",
            "total": 500
        }
    )

    orders.insert(
        "ORD002",
        {
            "customer": "Lan",
            "total": 800
        }
    )

    orders.insert(
        "ORD003",
        {
            "customer": "Huy",
            "total": 300
        }
    )

    print("\nTra cứu ORD002:")

    print(
        orders.get("ORD002")
    )

    print("\nXóa ORD003")

    orders.remove("ORD003")

    print("\nKiểm tra ORD003:")

    print(
        orders.get("ORD003")
    )


# ==================================================
# GROUP ANAGRAMS
# ==================================================

def group_coupon_anagrams(codes):

    groups = defaultdict(list)

    for code in codes:

        key = "".join(
            sorted(code)
        )

        groups[key].append(code)

    return list(groups.values())


# ==================================================
# LONGEST CONSECUTIVE
# ==================================================

def longest_consecutive_days(days):

    day_set = set(days)

    longest = 0

    for day in day_set:

        if day - 1 not in day_set:

            current = day

            length = 1

            while current + 1 in day_set:

                current += 1

                length += 1

            longest = max(
                longest,
                length
            )

    return longest


# ==================================================
# SUBARRAY SUM = K
# ==================================================

def count_revenue_windows(
        revenues,
        k):

    prefix_count = {0: 1}

    current_sum = 0

    count = 0

    for revenue in revenues:

        current_sum += revenue

        if current_sum - k in prefix_count:

            count += prefix_count[
                current_sum - k
            ]

        prefix_count[current_sum] = (
            prefix_count.get(
                current_sum,
                0
            ) + 1
        )

    return count


# ==================================================
# RABIN KARP
# ==================================================

BASE = 256
MOD = 1000000007


def rolling_hash_search(
        text,
        pattern):

    n = len(text)
    m = len(pattern)

    if m > n:
        return []

    result = []

    pattern_hash = 0
    window_hash = 0

    highest_power = 1

    for _ in range(m - 1):

        highest_power = (
            highest_power * BASE
        ) % MOD

    for i in range(m):

        pattern_hash = (
            pattern_hash * BASE
            + ord(pattern[i])
        ) % MOD

        window_hash = (
            window_hash * BASE
            + ord(text[i])
        ) % MOD

    for i in range(n - m + 1):

        if pattern_hash == window_hash:

            if text[i:i + m] == pattern:

                result.append(i)

        if i < n - m:

            left_char = ord(text[i])

            right_char = ord(
                text[i + m]
            )

            window_hash = (
                window_hash
                - left_char
                * highest_power
            ) % MOD

            window_hash = (
                window_hash * BASE
                + right_char
            ) % MOD

    return result


# ==================================================
# DEMO HASHING
# ==================================================

def demo_group_anagrams():

    print(
        "\n===== GROUP ANAGRAMS ====="
    )

    coupons = [
        "SAVE10",
        "AVES10",
        "HELLO",
        "OLLEH",
        "ABC"
    ]

    result = (
        group_coupon_anagrams(
            coupons
        )
    )

    for group in result:

        print(group)


def demo_longest_consecutive():

    print(
        "\n===== LONGEST CONSECUTIVE ====="
    )

    days = [
        100,
        4,
        200,
        1,
        3,
        2
    ]

    result = (
        longest_consecutive_days(
            days
        )
    )

    print("Danh sách:", days)

    print(
        "Chuỗi dài nhất:",
        result
    )


def demo_subarray_sum():

    print(
        "\n===== SUBARRAY SUM = K ====="
    )

    revenues = [
        1,
        1,
        1
    ]

    k = 2

    result = (
        count_revenue_windows(
            revenues,
            k
        )
    )

    print(
        "Doanh thu:",
        revenues
    )

    print("K =", k)

    print(
        "Số đoạn con:",
        result
    )


def demo_rolling_coupon_search():

    print(
        "\n===== RABIN-KARP ====="
    )

    text = (
        "SAVE10 SALE20 SAVE10 "
        "HELLO SAVE10"
    )

    pattern = "SAVE10"

    positions = (
        rolling_hash_search(
            text,
            pattern
        )
    )

    print(
        "Pattern:",
        pattern
    )

    print(
        "Vị trí xuất hiện:",
        positions
    )


def demo_hashing_problems():

    demo_group_anagrams()

    demo_longest_consecutive()

    demo_subarray_sum()