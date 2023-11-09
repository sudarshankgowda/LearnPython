if __name__=="__main__":
    n = int(input())
    set_A = set(map(int, input().split()[:n]))
    m = int(input())
    set_B = set(map(int, input().split()[:m]))
    set_AB = set_A.intersection(set_B)
    # for i in set_AB:
    #     print(i)
    print(len(set_AB))