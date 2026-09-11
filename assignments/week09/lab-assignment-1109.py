def calculate_electricity_cost(units):
    total = 0.00
    print("รายละเอียดค่าไฟ: ")
    if units > 0:
        u1 = min(units,50)
        cost1 = u1*2.50
        total += cost1
        print(f"1-50 หน่วย: {cost1} บาท")
    if units>50:
        u1 = min(units-50,50)
        cost2 = u1*3.00
        total += cost2
        print(f"51-100 หน่วย: {cost2} บาท")
    if units>100:
        u1 = min(units-100,50)
        cost3 = u1*3.50
        total += cost3
        print(f"101-200 หน่วย: {cost3} บาท")
    if units > 200:
        u1 = units-200
        cost4 = u1*4.00
        total += cost4
        print(f"มากกว่า 200 หน่วย: {cost4} บาท")
    total += 25
    print("ค่าบริการ: 25.00 บาท")
    print(f"รวมค่าไฟทั้งสิ้น: {total} บาท")
print("===== โปรแกรมคำนวณค่าไฟฟ้า =====")
print("1. คำนวณค่าไฟ")
print("2. ออกจากโปรแกรม")
while True:
    choice = input("เลือกเมนู: ")
    if choice == '1':
       units = float(input("กรอกจำนวนหน่วยไฟฟ้า: "))
       calculate_electricity_cost(units)
    else:
       break