if __name__=="__main__":
    n = int(input())
    setA = set(map(int, input().split()[:n]))
    m = int(input())

    for _ in range(m):
        operation, length = input().split()
        other_set = set(map(int, input().split()))
        if operation == "intersection_update":
            setA.intersection_update(other_set)
        elif operation == "update":
            setA.update(other_set)
        elif operation == "symmetric_difference_update":
            setA.symmetric_difference_update(other_set)
        elif operation == "difference_update":
            setA.difference_update(other_set)
print(sum(setA))