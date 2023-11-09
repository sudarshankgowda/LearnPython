if __name__=="__main__":
    n = int(input(""))
    curr_set = set()
    for i in range(n):
        curr_set.add(input())
    print(curr_set)
    print(len(curr_set))