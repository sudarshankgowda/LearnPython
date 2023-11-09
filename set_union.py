if __name__=="__main__":
    set_A = set()
    set_B = set()
    n = input()
    set_A = set(map(int, input().split()))
    m = input()
    set_B = set(map(int, input().split()))

    AB_union = set_A.union(set_B)

    # for i in AB_union:
    #     print(i)

    print(len(AB_union))