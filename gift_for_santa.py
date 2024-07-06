n = int(input())
m = int(input())
s = int(input())


for num in range(m + 1, n, -1):
    if num % 2 == 0 and num % 3 == 0:
        if num == s:
            break
        print(num, end=' ')
