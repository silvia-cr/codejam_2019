def main():
    t = int(input())

    for i in range(1, t+1):
        n = input()

        a = n.replace('4', '2')

        b = int(n) - int(a)
        print('Case #{0}: {1} {2}'.format(i, a, b))


if __name__ == '__main__':
    main()
