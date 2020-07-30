N = int(input())

def addnum(n):
    if n < 10:
        return n
    return n % 10 + addnum(n // 10)

print(addnum(N))