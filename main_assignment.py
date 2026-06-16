"""
main_assignment.py

Chương trình chính
DSA Assignment
"""

from routing import (
    demo_routing_shortest_path,
    demo_mst_network
)

from hashing_tools import (
    demo_order_hash_table,
    demo_hashing_problems,
    demo_rolling_coupon_search
)

from promo_optimizer import (
    demo_dp_basics,
    demo_combo_knapsack_2d,
    demo_combo_knapsack_1d
)


# ==========================================
# MENU
# ==========================================

def show_menu():

    print("\n" + "=" * 50)
    print("POLY SHIP - DSA ASSIGNMENT")
    print("=" * 50)

    print("1. Dijkstra Shortest Path")
    print("2. Kruskal MST")
    print("3. Order Hash Table")
    print("4. Hashing Problems")
    print("5. Rolling Hash (Rabin-Karp)")
    print("6. Dynamic Programming")
    print("7. Knapsack Optimization")
    print("8. Exit")


# ==========================================
# MAIN
# ==========================================

def main():

    while True:

        show_menu()

        choice = input(
            "\nNhập lựa chọn: "
        ).strip()

        try:

            if choice == "1":

                demo_routing_shortest_path()

            elif choice == "2":

                demo_mst_network()

            elif choice == "3":

                demo_order_hash_table()

            elif choice == "4":

                demo_hashing_problems()

            elif choice == "5":

                demo_rolling_coupon_search()

            elif choice == "6":

                demo_dp_basics()

            elif choice == "7":

                print(
                    "\n===== KNAPSACK ====="
                )

                demo_combo_knapsack_2d()

                demo_combo_knapsack_1d()

            elif choice == "8":

                print(
                    "\nKết thúc chương trình."
                )

                break

            else:

                print(
                    "\nLựa chọn không hợp lệ!"
                )

        except Exception as error:

            print(
                "\nCó lỗi xảy ra:"
            )

            print(error)


if __name__ == "__main__":
    main()