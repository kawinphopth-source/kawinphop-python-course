prices = []
print("Enter prices of 6 items:")
for i in range(1, 7):
    price = int(input(f"Item {i}: "))
    prices.append(price)
print()
budget = int(input("Enter total budget: "))
print()
current_total = 0
bought_items = []
for i in range(len(prices)):
    if current_total + prices[i] <= budget:
        status = "buy"
        current_total = current_total + prices[i]
        bought_items.append(prices[i])
    else:
        status = "cannot buy"
    print(f"Item {i+1} = {prices[i]} -> {status}")
    print(f"Current total = {current_total}")
    print()
print(f"Bought items: {bought_items}")
print(f"Total spent: {current_total}")
print(f"Remaining budget: {budget - current_total}")