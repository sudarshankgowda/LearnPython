def print_formatted(number):
    # your code goes here
    #print("Decimal Octal Hexa Binary")
    width = len("{0:b}".format(number))
    for i in range(number+1):
        print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)