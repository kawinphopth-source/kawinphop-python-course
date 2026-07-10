# Template 3: Shopping Calculator
shopping_calculator = '''
# Shopping Calculator Template

item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount %: "))
tax_percent = float(input("Enter tax %: "))

# TODO: Calculate subtotal
# TODO: Calculate discount amount
# TODO: Calculate price after discount
# TODO: Calculate tax amount
# TODO: Calculate final total
# TODO: Display itemized receipt
'''
#input
item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount %: "))
tax_percent = float(input("Enter tax %: "))
#process
subtotal = item_price*quantity
discount_amount = subtotal*(discount_percent/100)
price_after_discount = subtotal-discount_amount
tax_amount = subtotal*(tax_percent/100)
final_total =price_after_discount+tax_amount
#output
print(f"Subtotal = {subtotal}, Discount amount = {discount_amount}, Price after discount ={price_after_discount}, Tax amount = {tax_amount}, Final total = {final_total}")