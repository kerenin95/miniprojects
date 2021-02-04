'''Decimal to binary converter'''

# input decimal number
n = 50

# create function to convert the decimal number to binary
def dectobin(number):
    if number >= 1:
        dectobin(number // 2)
        print(number % 2, end= '')

print(dectobin(n))
# output for 5 should be 101