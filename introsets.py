def average(arr):
    return round(sum(set(arr)) / len(set(arr)), 3)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(f"set array is {set(arr)}")
    result = average(arr)
    print(result)

# 10
# 161 182 161 154 176 170 167 171 170 174
