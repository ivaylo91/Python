n = int(input())

def count_sheep(n):
    result = ""
    count = 1

    while count <= n:
        result += str(count) + " sheep..."
        count += 1
    print(result)

count_sheep(n)