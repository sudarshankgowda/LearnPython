if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(list(integer_list))
    t = tuple(integer_list)
    print(t)
    result = hash(t)
    print(result)