"""
เขียน FUNCTION แปลงหน่วยสกุลเเงิน ที่สามารถแปลงเงินจาก
THB <-> USD .. 1 USD = 32 THB
THB <-> JPY .. 100 JPY = 22 THB

โดยใช้ชื่อและการใช้งาน
function convert_currency(100,"USD")

แสดงผลออกทางหน้าจอ
100 THB = 3.3 USD

และทดสอบการใช้งาน function ที่ตัวเองเขียนด้วย

"""
def convert_currency(amount,currency):
    if currency == "USD":
        print("Choose conversion direction:")
        print("1: THB to USD")
        print("2: USD to THB")
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            print(f"{amount} THB = {amount/32.0:.2f} USD")
        elif choice == "2":
            print(f"{amount} USD = {amount*32.0:.2f} THB")
    elif currency == "JPY":
        print("Choose conversion direction:")
        print("1: THB to JPY")
        print("2: JPY to THB")
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            print(f"{amount} THB = {amount/22.0*100:.2f} JPY")
        elif choice == "2":
            print(f"{amount} JPY = {amount/100*22.0:.2f} THB")
convert_currency(1000,"JPY")