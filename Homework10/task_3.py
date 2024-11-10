def calculating_factorial(number):
    result = 1
    for i in range(number):
        result *= (i + 1)
    return result

print(calculating_factorial(2))
print(calculating_factorial(5))
print(calculating_factorial(1))
print(calculating_factorial(0))
print(calculating_factorial(12))