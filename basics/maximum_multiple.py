divisor = int(input())
bound = int(input())

for num in range(bound, divisor, -1):
    if num <= bound:
        if num % divisor == 0:
            if num > 0:
                print(num)
                break
