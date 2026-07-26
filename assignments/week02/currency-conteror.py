exchange_rate = 35.5 
print("Choose conversion direction:")
print("1: THB to USD")
print("2: USD to THB")
choice = input("Enter 1 or 2: ")
if choice in ["1", "2"]:
    amount = float(input("Enter the amount to convert: "))
if choice == "1":
        result = amount / exchange_rate
        print(f"Result: {result:.2f} USD")
        print(f"Formula used: {amount} THB / {exchange_rate} = {result:.2f} USD")
elif choice == "2":
        result = amount * exchange_rate
        print(f"Result: {result:.2f} THB")
        print(f"Formula used: {amount} USD * {exchange_rate} = {result:.2f} THB")
else:
    print("Invalid choice. Please run the program again and select 1 or 2.")