# binary_investigation.py

# decimal
n = 10
print (n)

# binary
n = 0b1000
print (n)

# hexadecimal
n = 0xFF
print (n)

# octal
n = 0o77
print (n)

print (f"{n}")
print (f"{n:b}")
print (f"{n:x}")
print (f"{n:o}")

# format with leading zeros
n = 0x80
print (f"{n:08b}")

# bitwise operators
n = 0x80
while n > 0:
    print (f"{n:08b}")
    # n = n >> 1
    n >>= 1


# shortcut assignment operators
n = 10
n = n + 10
n += 10


# you can specify a base when converting a string
bvalue = "10000010010101"
n = int(bvalue, base=2)
print (n)















