def main():
    t = int(input())

    for i in range(1, t + 1):
        n = int(input())
        p = input()

        p = p.replace('E', 's')
        p = p.replace('S', 'E')
        p = p.replace('s', 'S')

        print('Case #{0}: {1}'.format(i, p))


if __name__ == '__main__':
    main()
