if __name__=="__main__":
    setops = set()
    n = int(input())
    setops = set(map(int, input().split()[:n]))

    N=int(input())
    for _ in range(N):
        command=input().split()
        if command[0] == "pop":
            setops.pop()
            # l = list(setops)
            # l.reverse()
            # l.pop()
            # l.reverse()
            # setops = set(l)
        elif command[0] == "remove":
            setops.remove(int(command[1]))
        elif command[0] == "discard":
            setops.discard(int(command[1]))

    for i in setops:
        print(i)