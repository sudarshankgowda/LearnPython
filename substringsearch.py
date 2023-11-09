def count_substring(string, substring):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count
if __name__=='__main__':
    string = input("Enter the string :")
    substring = input('Enter the substring to be searched and counted in string :')
    print(count_substring(string, substring))
