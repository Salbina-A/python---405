def check_fact(n):
    f = 1
    i = 1
    while f < n:
        i += 1
        f *= i
    print(f)
print(check_fact(3))