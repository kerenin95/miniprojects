'''this takes a binary number and converts it to decimal'''

n = 101

def bintodec(num):
    binary = num
    decimal, i, n = 0,0,0
    while (num != 0):
        dec = num %10
        decimal = decimal + dec * pow(2, i)
        num = num//10
        i += 1
    print(decimal)

print(bintodec(n))