def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def get_prime_factors(result):
    for i in range(2, result):
        if result % i == 0 and is_prime(i):
            return i, result/i
    return 0, 0


def main():
    t = int(input())

    for i in range(1, t + 1):
        test_case = input().split()

        n = int(test_case[0])
        l = int(test_case[1])
        ciphertext_values = input().split()

        if len(ciphertext_values) != l:
            raise Exception

        first, second = get_prime_factors(int(ciphertext_values[0]))
        prime_numbers = list()

        if int(ciphertext_values[1]) % first == 0:
            prime_numbers.append(second)
            prime_numbers.append(first)
        else:
            prime_numbers.append(first)
            prime_numbers.append(second)

        for val in ciphertext_values[1:]:
            prime_numbers.append(int(val)/prime_numbers[-1])

        alphabet = sorted(list(set((prime_numbers))))
        word = list()

        for number in prime_numbers:
            idx = alphabet.index(number)
            word.append(chr(idx+65))

        print('Case #{0}: {1}'.format(i, ''.join(word)))


if __name__ == '__main__':
    main()
