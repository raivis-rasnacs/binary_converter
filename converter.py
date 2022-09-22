dec = int(input("Decimal number: "))
binary = ""

while dec > 0:
    binary += str(dec % 2)
    dec //= 2

print(binary[::-1])
