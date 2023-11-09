if __name__=='__main__':
    m, n = map(int, input().split())# n has to be 3 times the m.
    #M,N values are as follows - 3 9 or 9 27 etc.
    for i in range(1, m, 2):
        print(('.|.'*i).center(n, '-'))
    print(('WELCOME'.center(n,'-')))
    for i in range(m-2, -1, -2):
        print(('.|.'*i).center(n,'-'))

