def check_fact(n):
    fact = 1
    i = 1
    while fact < n:
        i += 1
        fact *= i
    print(fact)
print(check_fact(3))
