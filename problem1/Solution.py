def find_four(s):
    try:
        idx = s.index('4')
    except:
        idx = -1

    return idx


def main():
    t = int(input())

    for i in range(1,t+1):
        n = input()
        a = list(n)
        b = 0

        idx = find_four(a)

        while idx > -1:
            a[idx] = 2

            b += 2*10**(len(a)-idx-1)

            idx = find_four(a)

        a = map(str, a)
        print(f'Case #{i}: {"".join(a)} {str(b)}')


if __name__ == '__main__':
    main()


