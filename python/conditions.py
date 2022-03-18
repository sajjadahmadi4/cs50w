# practicing conditions

# no matter what you enter, the input function
# always store it as str
# n = input("Number: ")

n = int(input("Number: "))

if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")