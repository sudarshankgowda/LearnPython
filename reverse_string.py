def reverse_string(sentence):
    newchar = " "
    for char in sentence:
        newchar = char  + newchar
    return newchar
    
print(reverse_string("hello"))  

def reverse_string(sentence1):
    char = sentence1.split()
    newchar = []
    for char in sentence1[::-1]:
        newchar.append(char)
    return  "".join(newchar)

print(reverse_string("Bhuvi")) 



