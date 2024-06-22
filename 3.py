def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime_factor(number):
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
    return number

if __name__ == "__main__":
    target_number = 600851475143
    largest_prime = largest_prime_factor(target_number)
    print("The largest prime factor of", target_number, "is:", largest_prime)
