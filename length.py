digit = int(input("What is the number you want to use?:"))
count = 0
while digit > 0:
    num = digit%10
    if num >= 0:
        count = count + 1    
    digit = digit//10
print(f"Number of digits is {count}")
