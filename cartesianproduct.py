# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=='__main__':
    list_A = list(map(int, input("Enter the contents of list A: ").split()))
    list_B = list(map(int, input("Enter the contents of list B: ").split()))

    list_AB = []
    for i in list_A:
        for j in list_B:
            list_AB.append((i, j))
    for i in list_AB:
        print(f"{i}", end=" ")