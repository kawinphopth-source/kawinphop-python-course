def deposit(money):
    initial_balance = 1000
    try:
        amount = float(money)
        if amount <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")
    except ValueError as e:
        if str(e) == "จำนวนเงินฝากต้องมากกว่า 0":
            print(f"เกิดข้อผิดพลาด: {e}")
        else:
            print("เกิดข้อผิดพลาด: ข้อมูลที่กรอกต้องเป็นตัวเลขเท่านั้น")
    else:
        new_balance = initial_balance + amount
        print("ฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {new_balance:.2f} บาท")
    finally:
        print("สิ้นสุดรายการฝากเงิน")
print("ยอดเงินเริ่มต้น: 1000 บาท")
user_input = input("กรอกจำนวนเงินที่ต้องการฝาก: ")
print()
deposit(user_input)