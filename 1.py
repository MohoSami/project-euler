def sum_multiples_of_3_and_5(limit):
    total = 0
    for num in range(1, limit):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    return total

# Call the function with the limit of 1000
result = sum_multiples_of_3_and_5(1000)
print(result)