if __name__=='__main__':
    mylist=[]
    N = int(input("Enter the N number of operation to perform on list: "))

    for _ in range(N):
        command, *args=input().split()
        if command == 'insert':
            mylist.insert(int(args[0]), int(args[1]))
        elif command == 'print':
            print(mylist)
        elif command == 'remove':
            mylist.remove(int(args[0]))
        elif command == 'append':
            mylist.append(int(args[0]))
        elif command == 'sort':
            mylist.sort()
        elif command == 'pop':
            mylist.pop()
        elif command == 'reverse':
            mylist.reverse()

