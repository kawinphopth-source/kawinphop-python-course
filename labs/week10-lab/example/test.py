"""
print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = 'Hello World'
for letter in text:
    if letter == 'l':
        count += 1
print(f"{count} letters 'l' found in '{text}'")
"""

# 1. รับค่า text จากผู้ใช้
# 2. รับค่าอักขระที่ต้องการค้นหาจากผู้ใช้
# 3. แสดงผลจำนวนของอักขระในข้อความ text

text = input("Insert your text: ")
char = input("Character to find: ")
count = 0
for letter in text:
    if letter == char:
        count += 1
print(f"{count} letters '{char}' found in '{text}'")

# เขียนโปรแกรมตรวจสอบความแข็งแรงของ PASSWORD
# นิยามของ strong password คือ ยาวมากกว่า 8 ตัว, มีอักขระ @ 1 ตัว, มีตัวเลข, มีตัวอักษร

password = input("Insert your password: ")
length = len(password)
words = password.split('@')

if len(words) > 1 and password.count('@') == 1:
    left = words[0].isalnum()
    right = words[1].isalnum()
else:
    left = False;
    right = False;
if length >= 8 and password.count('@') == 1 and left == True and right == True:
    print("Your password is strong!")
else:
    print("Your password is not strong!")