if __name__ == '__main__':
    n = int(input("Please enter the value of n : "))
    print(f"The number n is : {n}")
    print(f"Enter the {n} elements one by one with space in single line : ", end="")
    arr1 = map(int, input().split())
    arr = list(arr1)
    print(arr)
    mx = max(arr[0], arr[1])
    secondMax = min(arr[0], arr[1])
    for i in range(2,n):
        if (arr[i] > mx):
            secondMax = mx
            mx = arr[i]
        elif (arr[i] > secondMax and mx != arr[i]):   # 3 5 4 1
            secondMax = arr[i]
        elif (mx == secondMax and secondMax != arr[i]): # 4 4 3 2
            secondMax = arr[i]
    print(secondMax)