def find_four(s):
    try:
        idx = s.index('4')
    except:
        idx = -1

    return idx


def main():
    t = int(input())

    for i in range(1, t+1):
        n = input()
        a = list(n)

        idx = find_four(a)

        while idx > -1:
            a[idx] = 2
            idx = find_four(a)

        a = ''.join(map(str, a))
        b = int(n) - int(a)
        print('Case #{0}: {1} {2}'.format(i, a, b))


if __name__ == '__main__':
    main()
