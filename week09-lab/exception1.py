try:
    num1 = float(input("ตัวเลขที่ 1: "))
    num2 = float(input("ตัวเลขที่ 2: "))
    operator = input("เครื่องหมาย (+,-,*,/): ")
    result = 0
    if operator == '+':
        result = num1+num2
    elif operator == '-':
        result = num1-num2
    elif operator == '*':
        result = num1*num2
    elif operator == '/':
        result = num1/num2
    else:
        raise ValueError("เครื่องหมายต้องเป็น +,-,*,/ เท่านั้น")
    print(f"\nผลลัพธ์ = {result}")
except ValueError as error:
    print(f"\nกรอกตัวเลขให้ถูกต้อง {error}")
except ZeroDivisionError:
    print("\nไม่สามารถหารด้วยศูนย์ได้")
finally:
    print("จบการทำงาน")