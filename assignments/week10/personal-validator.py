"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""
print("\n=== PERSONAL INFORMATION VALIDATION ===")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
phone = input("Enter your phone number: ")
print("\nValidation Results:")
check_name = False
for char in name:
    if char.isalpha() or char.isspace():
        check_name = True
    else:
        check_name = False
check_age = False
if check_name:
    print("Name: Valid (contains only letters and spaces)")
else:
    print("Name Invalid")
if 18 <= age <= 65:
    check_age = True
    print(f"Age: Valid ({age} years old)")
check_phone = False
if phone.isdigit() and len(phone) == 10:
    check_phone = True
    print("Phone: Valid (10-digit number)")
print("\nFormatted Information:")
print(f"Name: {name.upper()}")
if 18 <= age <= 30:
    print("Age Group: Young Adult (18-30)")
else:
    print("Age Group: Old Adult (31-65)")
print(f"Phone: +91-{phone}")