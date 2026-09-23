# ERROR (bugs)
# 3 types => syntax errors / runtime error / logic error

#ValueError Exception
try:
    age = int(input("กรอกอายุ: "))
    print(f"ปีหน้าคุณจะอายุ {age + 1} ปี")
except ValueError:
    print("กรุณากรอกอายุเป็นตัวเลขจำนวนเต็ม เช่น 20")

#ZeroDivisionExeption
try:
    numerator = float(input("กรอกตัวตั้ง: "))
    denominator = float(input("กรอกตัวหาร: "))

    result = numerator / denominator
    print(f"ผลลัพธ์ = {result}")
except ValueError:
    print("กรอกตัวเลขให้ถูกต้อง")

except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")

#FileNotFoundException, PermissionException
try:
    filename = input("ชื่อไฟล์: ")
    
    with open(filename, "r", encoding= "utf-8") as file:
        content = file.read()

    print("เนื้อหาถูกต้อง")
    print(content)

except FileNotFoundError:
    print(f"ไฟล์ไม่พบ {filename}")

except PermissionError:
    print("ไม่มีสิทธิ์เข้าถึงไฟล์นี้")

# raise ใช้สำหรับ ส่งให้ Python สร้าง Exception ขึ้นเอง เมื่อข้อมูลหรือสถานการณ์ไม่เป็นไปตาม
# แม้คำสั่งนั้นจะไม่ผิดไวยากรณ์และ Python ยังทำงานต่อได้ตามปกติก็ตาม

try:
    score = float(input("กรอกคะแนน 0-100: "))

    if not 0 <= score <= 100: # score >= 0 and score <= 100 ที่อื่นต้องเขียนแบบนี้ ไม่งั้นโดนตบ!!!
        raise ValueError("คะแนนต้องอยู่ระหว่าง 0 ถึง 100")
    
except ValueError as error:
    print(f"ข้อมูลไม่ถูกต้อง: {error}")

else:
    print(f"บันทึกคะแนน {score} เรียบร้อย")

finally: # Do it everytime at last process in code
    print("จบการตรวจสอบคะแนน")