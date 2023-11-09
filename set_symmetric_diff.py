if __name__=="__main__":
    n = int(input())
    setA=set(map(int, input().split()[:n]))
    m = int(input())
    setB=set(map(int, input().split()[:m]))

    setAB = setA.symmetric_difference(setB)
    print(len(setAB))