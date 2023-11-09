import string
def rangoli_new(size):
    alpha = string.ascii_lowercase
    width = 4*size-3

    for i in range (size-1, -size, -1):
        x = abs(i)
        line = '-'.join((alpha[size-1:x:-1]) + alpha[x:size])
        print(line.center(width, "-"))


if __name__=='__main__':
    size = int(input("Enter the value of size :"))
    rangoli_new(size)