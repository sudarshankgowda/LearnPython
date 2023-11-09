import os
# Complete the solve function below.
def solve(s):
    return s.title()
    # name_list = s.split(" ")
    # capitalized_name_list = [name.capitalize() for name in name_list]
    # capitalized_full_name = " ".join(capitalized_name_list)
    # return capitalized_full_name

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)