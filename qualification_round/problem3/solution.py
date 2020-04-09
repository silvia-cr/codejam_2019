from math import gcd


def main():
    t = int(input())

    for i in range(1, t + 1):
        test_case = input().split()

        n = int(test_case[0])
        l = int(test_case[1])
        ciphertext_values = input().split()

        if len(ciphertext_values) != l:
            raise Exception

        greatest_common_divisor = gcd(int(ciphertext_values[0]), int(ciphertext_values[1]))

        prime_numbers = list()
        prime_numbers.append(int(ciphertext_values[0])/greatest_common_divisor)
        prime_numbers.append(greatest_common_divisor)

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
