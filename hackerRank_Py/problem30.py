import sys
from collections import Counter


def main():
    # Fast input reading
    input_line = sys.stdin.readline

    # Step 1: Read number of shoes (we can skip saving this variable)
    input_line()

    # Step 2: Create inventory counter directly from the space-separated string
    inventory = Counter(map(int, input_line().split()))

    # Step 3: Read number of customers
    num_customers = int(input_line())

    total_earned = 0

    # Step 4: Process each customer instantly
    for _ in range(num_customers):
        size, price = map(int, input_line().split())

        # If the size is in stock, sell it
        if inventory[size] > 0:
            total_earned += price
            inventory[size] -= 1  # Reduce stock

    print(total_earned)


if __name__ == "__main__":
    main()



