if __name__ == '__main__':
    M = int(input())
    set_m = set(map(int, input().split()))
    N = int(input())
    set_n = set(map(int, input().split()))
    for i in sorted((set_m.difference(set_n)).union(set_n.difference(set_m))):
        print(i)
