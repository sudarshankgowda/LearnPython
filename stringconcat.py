# if __name__=='__main__':
#     string="abracadabra"
#     #s=input("Enter string :")
#     l = list(string)
#     l[2] = 'd'
#     string=''.join(l)
#     print(f"string is {string}")

def mutable_string(string, position, character):
    return string[:position]+character+string[position+1:]

if __name__=='__main__':
    s=input()
    i,c=input().split()
    s_new=mutable_string(s, int(i), c)
    prite(s_new)