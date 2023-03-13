n, m, k = int(input(">>> ")), int(input(">>> ")), int(input(">>> "))

if k == n or k == m or k % m == 0 or k % n == 0:
    print("yes")
else:
    print("no")
