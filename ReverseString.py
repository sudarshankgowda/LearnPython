# txt = "Hello World"[::-1]
# print(txt)

# s = input("Enter the string to be reversed :")
# print(s[::-1])

# def reverse(string):
#     s = ""
#     for i in string:
#         s = i + s
#     return s
# s = input()
# print(reverse(s))

# def reverse(s):
#     if (len(s)) == 0:
#         return s
#     else:
#         return reverse(s[1:]) + s[0]
# s="GeeksforGeeks"
# print(reverse(s))

# def reverse(string):
#     print("".join(reversed(string)))
# s="GeeksforGeeks"
# reverse(s)

# def reverse(string):
#     liststr = list(string)
#     liststr.reverse()
#     print("".join(liststr))
#
# reverse("Sudarshan")

def reverse_using_while(string):
    s=""
    length = len(string) - 1
    print(length)
    while length >= 0:
        s = s + string[length]
        length = length-1
    return s

print(reverse_using_while("Sudarshan"))
