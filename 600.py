MOD = 10**9 + 7

def calculate_H(n):
    if n < 6:
        return 0
    elif n == 6:
        return 1
    
    H = [0] * (n + 1)
    H[6] = 1
    H[12] = 10

    for i in range(13, n + 1):
        H[i] = (3 * H[i-1] - H[i-2] + 3 * H[i-3] - H[i-4]) % MOD

    return H[n]

target_n = 55106
result = calculate_H(target_n)
print("H({}) = {}".format(target_n, result))
