# Stack
# class stack:
#     def __init__(self):
#         self.stack = []
    
#     def push(self, value):
#         self.stack.append(value)
    
#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         else:
#             print("stack is empty")
#             return None

#     def is_empty(self):
#         return len(self.stack) == 0
    
#     def display(self):
#         if not self.is_empty():
#             print("Stack elements are : ")
#             for i in self.stack:
#                 print(i)
#         else:
#             print("List is empty")

# st = stack()
# st.push(10)
# st.push(20)
# st.push(30)
# st.display()
# print(f"poped value : {st.pop()}")
# print(f"poped value : {st.pop()}")
# print(f"poped value : {st.pop()}")
# print(f"poped value : {st.pop()}")
# st.display()

# #===========================================================================================================================================
# Queue
# from collections import deque

# class Q:
#     def __init__(self):
#         self.queue =  deque()

#     def enqueue(self, item):
#         self.queue.append(item)

#     def dequeue(self):
#         if not self.is_empty():
#             return self.queue.popleft()
#         else:
#             print("Queue is empty")
#             return None
    
#     def is_empty(self):
#         return len(self.queue) == 0
    
#     def display(self):
#         if not self.is_empty():
#             print("Elements are :")
#             for i in self.queue:
#                 print(i)
#         else:
#             print("Q is empty")

# q = Q()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.display()
# print(f"dequeued item =  {q.dequeue()}")
# print(f"dequeued item =  {q.dequeue()}")
# q.display()

# #===========================================================================================================================================
# tuples = [(1, "one"), (2, "two")]
# dictionaries = dict(tuples)
# print(tuples)

# print("After conversion to dictionaries : ")
# for key, value in dictionaries.items():
#     print(f"{key}: {value}")

# #===========================================================================================================================================
# string = "madam" #input("Please enter the palindrome string: ")
# if string == string[::-1]:
#     print("String is palindrome")
# else:
#     print("The string is not palindrome")
# #===========================================================================================================================================
# #Decorator Example 

# def tryprint(numtries):
#     def decorator_repeat(func):
#         def wrapper(*args, **kwargs):
#             for i in range(numtries):
#                 func(*args, **kwargs)
#                 print(f"args : {args} and {kwargs}")
#                 #print("I wish all the best")
#         wrapper.original_function=func
#         return wrapper
#     return decorator_repeat

# @tryprint(numtries=3)
# def greet(name):
#     print(f"Welcome {name}")

# greet("Ashwini")

# print("========================Done with new one=======================")
# greet.original_function("Ashwini")
# print("================================================================")
# #===========================================================================================================================================
# dict1_simple = [{'name': 'Sud', 'age': 36}, {'name': 'Kau', 'age': 3}, {'name': 'Ash', 'age': 31}, {'name': 'Bhu', 'age': 5}]
# print(sorted(dict1_simple, key = lambda x:x["age"]))

# simple = {"Sud":36, "Ash":31, "Kau":3, "Bhu":5}
# simpledict = list(simple.items())
# converteddict=dict(sorted(simpledict, key=lambda x:x[1]))
# print(converteddict)
# #===========================================================================================================================================

# simple_dict=[{"name":"sudarshan", "age":36},{"name":"ashwini", "age":31}, {"name":"bhuvith", "age":5},{"name":"kaustubh", "age":3}]
# print(sorted(simple_dict, key = lambda x : x["age"]))

# sampledict = {"sudarshan":36, "ashwini":31, "bhuvith":5, "kaustubh":3}
# list_sampledict = list(sampledict.items())
# print(sorted(list_sampledict, key = lambda x : x[1]))

# #===========================================================================================================================================
# #custom Exception
# #How do you handle exceptions in Python?
# class InsufficientBalanceError(Exception):
#     def __init__(self, balance, withdraw):
#         self.balance = balance
#         self.withdraw = withdraw
#         super().__init__(f"{withdraw} amount is greater than the {balance}")

# class BankAccount():
#     def __init__(self, balance):
#         self.balance = balance

#     def withdraw(self, amount):
#         if self.balance < amount:
#             raise InsufficientBalanceError(self.balance, amount)
#         else:
#             self.balance = self.balance - amount
        
#         return self.balance

# try:
#     account = BankAccount(100)
#     print(f"current balance = {account.balance}")

#     account.withdraw(500)
# except InsufficientBalanceError as e:
#     print("Exception raised")
#     print(e)
# #===========================================================================================================================================
# #What is the purpose of the `finally` clause in exception handling?
# def read_file(filename):
#     try:
#         file = open(filename, "r")
#         data = file.read()
#         return data
#     except NameError:
#         print("Error : File not found")
#     except IOError:
#         print("Error : Input output error")
#     finally:
#         try:
#             file.close(data)
#         except NameError:
#             print("Error : File is not opened")
#             pass
#         except Exception as e:
#             print(f"Unexpected error: {e}")
#         print("Finally block executed")


# contents = read_file("bitwise.c")
# #print(contents)
# #===========================================================================================================================================

# #write file data daily to the file
#import multiprocessing.process
# import os
# import datetime

# directory = "UpdateToday"
# filepath = os.path.join(directory, "test.txt")

# if not os.path.exists(directory):
#     os.makedirs(directory)

# data = f"Today date is {datetime.datetime.now()}\n"

# #with open(filepath, "a") as file:
# #    file.write(data)
# file = open(filepath, "a")
# file.write(data)
# print("Data written succesfully")
# #===========================================================================================================================================
# import requests
# from bs4 import BeautifulSoup

# # URL of the webpage to scrape
# url = "https://www.example.com"

# # Send a GET request to the webpage
# response = requests.get(url)

# # Parse the webpage content
# soup = BeautifulSoup(response.content, 'html.parser')

# # Extract the title of the webpage
# title = soup.title.string

# print("Webpage Title:", title)
# #===========================================================================================================================================
# # How to create virtual enviroment
# # python -m venv myenv
# # myenv\scripts\activate
# # pip install package_name
# # deactivate
# # pip freeze > requirements.txt

# # or using virtualenv
# #pip install virtualenv
# #virtualenv myenv


# # Imagine you are working on web application and it needs particular version of python libraries.
# #1. Set Up the Virtual Environment:
# #python -m venv webapp_env
# #source webapp_env/bin/activate

# #2. Install Required Packages:
# #pip install flash sqlalchemy

# #3. Develop Your Application:
# #Create your application files, such as app.py, and start development using the installed packages.

# #4. List Installed Packages:
# #pip freeze > requirements.txt

# #5. Deploy or Share the Project:
# # Share the project directory with requirements.txt. The recipient can recreate the environment

# #python -m venv webapp_env
# #source webapp_env/bin/activate
# #pip install -r requirements.txt

# #6. Run the Application:
# #python app.py
# #===========================================================================================================================================

# #How would you read and write large files in Python?
# # 1. read the contents line by line
# # 2. read the contents chunk by chunk
# import os
# import subprocess
# filepath1 = os.path.join(os.getcwd(), "NVMe.txt")
# print(filepath1)
# chunk_size = 1024
# with open(filepath1, "r") as file:
#     #for line in file:
#     #print(line.strip())
#     while(True):
#         chunk = file.read(chunk_size)
#         if not chunk:
#             break
#         print(chunk)

# file.close()

# #===========================================================================================================================================
# binary_data = b"This is some binary data."

# with open("example.bin", "wb") as binary_file:
#     binary_file.write(binary_data)
# print("Data is written to the binary file successfully")
# #===========================================================================================================================================
# import struct

# # Packing data into binary format
# packed_data = struct.pack('iif', 1, 2, 3.0)
# print(packed_data)

# # Unpacking binary data into Python values
# unpacked_data = struct.unpack('iif', packed_data)
# print(unpacked_data)

# #===========================================================================================================================================
# import numpy as np
# a = np.array([1,2,3,4,5,6])
# print(np.sum(a))
# #===========================================================================================================================================

# def read_large_file(file_path):
#     with open(file_path, "r") as file:
#         for line in file:
#             yield line

# for line in read_large_file("NVMe.txt"):
#     print(line)
# #===========================================================================================================================================

# import numpy as np

# arr1 = np.array([1,2,3,4])
# print(f"numpy array : {arr1}")

# arr2 = np.array([[1,2,3], [4,5,6]])
# print(arr2)
# arr3 = np.arange(0,8,2)
# print(arr3)

# zeros = np.zeros((2,3))
# print(zeros)

# ones = np.ones((3,2))
# print(ones)
# #===========================================================================================================================================
# sum1 = arr1 + arr3
# print(f"add : {sum1}")

# multi = arr1 * arr3
# print(f"multi : {multi}")

# arr4 = np.dot(arr2, arr2.T)
# print(f"{arr4}")

# mean = np.mean(arr1)
# print(f"mean value : {mean}")

# max_value = np.max(arr1)
# print(f"Max_Value: {max_value}")

# std_dev = np.std(arr1)
# print(f"std deviation : {std_dev}")

# print(f"array1 : {arr1}")
# print(f"Slicing Ex : {arr1[1:3]}")


# random_no = np.random.rand(5)
# print(f"random no : {random_no}")

# random_nums = np.random.randint(1, 10, size=5)
# print(f"Random Numbers : {random_nums}")
# #=================================================================================================================================================

# import threading

# def print_data(chunk):
#     print(f"The chunk data is {chunk}")

# threads = []
# chunks = [2,3,4,5,6,7,8,9]

# for chunk in chunks:
#     thread = threading.Thread(target=print_data, args=(chunk,))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()
# #=================================================================================================================================================
# import multiprocessing

# def print_process_data(chunk):
#     print(f"The chunk data from process : {chunk}")

# chunks = [1,2,3,4,5,6,7,8,9]
# if __name__=="__main__":
#     processes = []
#     for chunk in chunks:
#         process = multiprocessing.Process(target=print_process_data, args=(chunk,))
#         processes.append(process)
#         process.start()

#     for process in processes:
#         process.join()
#=================================================================================================================================================
# Reversed words in sentence

# def reverse_sentence(sentence):
#     words = sentence.split()
#     rev_words = words[::-1]
#     return " ".join(rev_words)


# def reverse_sentence1(sentence):
#     words = sentence.split()
#     rev_words = []
#     for word in words[::-1]:
#         rev_words.append(word)
#     return ' '.join(rev_words)


# def reverse_sentence2(sentence):
#     return ' '.join(word for word in sentence.split()[::-1])

# sentence = "Google become old and chat gpt is new"
# #print(reverse_sentence(sentence))
# #print(reverse_sentence1(sentence))
# print(reverse_sentence2(sentence))
#=================================================================================================================================================

# def reverse_string(sentence):
#     return sentence[::-1]


# def reverse_string1(sentence):
#     newsent = ""
#     for char in sentence:
#         newsent = char + newsent
#     return newsent
    
# def reverse_string2(sentence):
#     return ''.join(reversed(sentence))

# def rec_reverse(s):
#     if len(s) == 0:
#         return s
#     else:
#         return rec_reverse(s[1:]) + s[0]

# print(f"Revesed string : {rec_reverse('home work')}")
# #=================================================================================================================================================
# #Write a Python function to count the frequency of each character in a string.
# from collections import Counter
# string = "Home work"
# localdict = Counter(string)
# for key, value in localdict.items():
#     print(f"key : {key} and value : {value}")

#=================================================================================================================================================
# Generate fibonacci
# num = 10

# def gen_fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a+b

# fib = gen_fibonacci()
# for i in range(num):
#     print(next(fib))
#=================================================================================================================================================
# Generate the prime numbers 
# def check_prime_num(num):
#     if num < 2:
#         return False
    
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             return False
#     return True

# def gen_prime():
#     n = 2
#     while True:
#         if check_prime_num(n):
#             yield n
#         n = n + 1

# prime = gen_prime()

# for i in range(21):
#     print(next(prime))

#=================================================================================================================================================
# def decorator_fun(fun):
#     def wrapper():
#         print("Before")
#         fun()
#         print("After")
#     return wrapper

# @decorator_fun
# def greet():
#     print("Welcome")
#=================================================================================================================================================

# def outer_fun(x):
#     def inner_fun(y):
#         print(f"y is {y}")
#         return x+y
#     return inner_fun

# closure = outer_fun(3)

# print(closure(4))
#=================================================================================================================================================
# def fun(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(f"key : {key}, value : {value}")

# fun(1,2,3, name="Sudarshan", age=36)
#=================================================================================================================================================

# import unittest

# class mathOps(unittest.TestCase):
#     def setUp(self):
#         self.a = 10
#         self.b = 20
#         print(f"Initialization")
    
#     def testmethod(self):
#         print(f"Test is under Execution")
#         print(f"a : {self.a}, b : {self.b}")

#     def tearDown(self):
#         print("Releasing the memory allocated")
#         del self.a
#         del self.b

# if __name__=="__main__":
#     unittest.main()
#=================================================================================================================================================
# Write a Python function to count the frequency of each character in a string.

# sentence = "Welcome to micron"
# chars = [x for x in sentence]
# print(chars)

# simpledict = dict()
# for char in chars:
#     if char not in simpledict:
#         simpledict[char]=1
#     else:
#         simpledict[char] = simpledict[char] + 1


# for key, value in simpledict.items():
#     print(f"key : {key} -> value : {value}")

#=================================================================================================================================================
# Anagram Check
# from collections import Counter
# def are_anagrams(str1, str2):
#     # Remove spaces and convert to lowercase
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()

#     # If lengths are different, they cannot be anagrams
#     if len(str1) != len(str2):
#         return False

#     # Create frequency dictionaries for both strings
#     frequency_1 = {}
#     frequency_2 = {}
#     frequency_1 = Counter(str1)
#     frequency_2 = Counter(str2)
#     return frequency_1 == frequency_2

# # Example usage:
# print(are_anagrams("listenn", "silennt"))  # True
# print(are_anagrams("hello", "world"))    # False
#=================================================================================================================================================
# #Fibonacci Sequence
# num = int(input("Enter the number : "))
# def gen_fibonacci():
#     a, b = 1, 0
#     while 1:
#        yield a
#        a, b = b, a+b

# fib = gen_fibonacci()

# for i in range(num):
#     print(next(fib))
#==============================================================================================================================================
# Prime Number Check : Write a function to check if a number is prime.
# def check_prime_number(num):
#     if num < 2:
#         return False
    
#     for i in range(2, int(num**0.5)+1):
#         if num%i == 0:
#             return False
#     return True

# def gen_prime():
#     n = 2
#     while True:
#         if check_prime_number(n) :
#             yield n
#         n = n + 1

# prime = gen_prime()

# for i in range (1):
#     print(next(prime))

# print(f"Is 3637 a prime number ? : {check_prime_number(3637)}")
#==============================================================================================================================================
#Find the duplicates in list 
#Case 1
# mylist = [1,2,3,4,5,6,7,8,9,2,3,6]
# dup = {}
# for item in mylist:
#     if item not in dup:
#         dup[item] = 1
#     else:
#         dup[item] = dup[item] + 1

# for key, value in dup.items():
#     if value >= 2:
#         print(f"key : {key}, Value : {value}")

# print("===============================================================================================")
# #Case 2 
# from collections import Counter
# duplist = Counter(mylist)

# for key, value in duplist.items():
#     print(f"key : {key}, Value : {value}")
# #==============================================================================================================================================
# Find the max and min in list
# numlist  = [1,2,3,4,5,6,7,8,9,0,33,55,67,71,10,43]
# print(f"Min Number : {min(numlist)}, Max Number : {max(numlist)}")
# #==============================================================================================================================================
# def find_min_max(numlist):
#       if not numlist:
#         return None, None
#       min = max = numlist[0]
#       for num in numlist:
#             if min > num:
#                 min = num
#             if max < num:
#                 max = num
#       return min, max

# minimum, maximum = find_min_max(numlist)
# print(f"Minimum : {minimum}, Maximum : {maximum}") 
#==============================================================================================================================================
# Sum of Digits: Write a function to find the sum of the digits of a number.
# nlist = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for num in nlist:
#     sum += num
# print(sum)
# #==============================================================================================================================================
# # *Factorial of a Number*: Write a function to find the factorial of a number.
# def fact(num):
#     mul = 1
#     for each in range(1,num+1):
#         mul = mul * each
#     return mul

# print(f"factorial value :  {fact(5)}")

# def fact(num):
#     if num < 0:
#         print("factorial is not possible for negative number")
#     if num == 0 or num == 1:
#         return 1
#     return num * fact(num -1)   

# print(fact(5)) 

#==============================================================================================================================================
# Merge Two Sorted Lists
# list1 = [1,3,5,7,9]
# list2 = [2,4,6,8]
# mergedlist = [1, 2, 3, 4, 5, 6, 7, 8]
# i = 0
# j = 0

# while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             mergedlist.append(list1[i])
#             i = i+1
#         else:
#             mergedlist.append(list2[j])
#             j = j+1

# while i < len(list1):
#      mergedlist.append(list1[i])
#      i = i + 1

# while j < len(list2):
#      mergedlist.append(list2[i])
#      j = j + 1

# print(mergedlist)
#==============================================================================================================================================
# def is_balanced(s):
#     stack = []
#     matching_chars = { ')' : '(', '}': '{', ']' : '['}
    
#     for char in s:
#         if char in "[{(":
#             stack.append(char)
#         elif char in ')}]':
#             if not stack or stack[-1] != matching_chars[char]:
#                 return False
#             stack.pop()

#     return len(stack) == 0

# print(f"verify the brackets :", is_balanced("({[]})"))
# print(f"Verify the brackets :", is_balanced("({})"))

#==============================================================================================================================================
# # Find the Missing Number in a List: Given a list of n-1 integers in the range from 1 to n, find the missing number

# missinglist = [1,2,3,4,5,6,7,9]
# def find_missing_num(lst):
#     n = len(lst)+1
#     total_sum = (n*(n+1))//2
#     missing_num = total_sum - (sum(lst))
#     return missing_num

# print(f"missing_element = {find_missing_num(missinglist)}")
#==============================================================================================================================================

# def find_common_prefix(strlist):
    
#     strlist.sort()
#     i = 0
#     first = strlist[0]
#     last  = strlist[-1]
#     while i < len(first) and i < len(last) and (first[i] == last[i]):
#         i = i + 1

#     return first[:i]

# strlist = ["flower", "flow", "flight"]

# print(f"common prefix : {find_common_prefix(strlist)}")
# #==============================================================================================================================================
# *Find the Intersection of Two Lists*: Write a function to find the intersection of two lists.

# list1 = [1,2,3,4,5]
# list2 = [4,5,6,7,8,9]

# ilist = [item for item in list1 if item in list2]
# print(f"Intersection of list : ", ilist)
# #==============================================================================================================================================
# # *Remove Duplicates from a List*: Write a function to remove duplicate elements from a list.

# def remove_duplicates(input_list):
#     return list(set(input_list))

# # Example usage:
# input_list = [1, 6, 2, 2, 3, 4, 4, 5]
# print(f"List without duplicates: {remove_duplicates(input_list)}")

# #==============================================================================================================================================
# def remove_dup(input_list):
#     dup = []

#     for item in input_list:
#         if item not in dup:
#             dup.append(item)
    
#     return dup

# print(f"After removing the duplicates : {remove_dup(input_list)}")

#==============================================================================================================================================
# def kadane_algorithm(arr):
#     max_current = max_global = arr[0]
#     for i in range(1, len(arr)):
#         max_current = max( arr[i], max_current + arr[i])
#         if max_current > max_global:
#             max_global = max_current

#     return max_global

# # Example usage:
# array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(f"The largest sum contiguous subarray is: {kadane_algorithm(array)}")
# #==============================================================================================================================================
# # *Transpose a Matrix*: Write a function to transpose a given matrix.

# def transpose(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0])

#     transposed_matrix = []
#     for i in range(cols):
#         new_row = []
#         for j in range(rows):
#             new_row.append(matrix[j][i])
#         transposed_matrix.append(new_row)

#     return transposed_matrix

# matrix = [[1,2,3,4],
#           [5,6,7,8],
#           [9,10,11,12]
#           ]

# transposed_matrix = transpose(matrix)

# for row in transposed_matrix:
#     print(row)

#==============================================================================================================================================
# *Rotate an Array*: Write a function to rotate an array by k positions

# def rotate_array(arr, pos):
#     k = pos % len(arr)
#     return arr[-k:] + arr[:-k]

# arr = [1,2,3,4,5,6,7,8,9] 

# print(f"rotating array : {rotate_array(arr, 3)}")

#==============================================================================================================================================

# *Find the Longest Palindromic Substring*: Given a string, find the longest substring that is a palindrome.

# def longest_palindromic_substring(s):
#     if len(s) == 0:
#         return ""

#     def expand_around_center(s, left, right):
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             left -= 1
#             right += 1
#         return s[left + 1:right]

#     longest = ""
#     for i in range(len(s)):
#         # Odd length palindromes (center at one character)
#         temp = expand_around_center(s, i, i)
#         if len(temp) > len(longest):
#             longest = temp
#         # Even length palindromes (center between two characters)
#         temp = expand_around_center(s, i, i + 1)
#         if len(temp) > len(longest):
#             longest = temp

#     return longest

# # Example usage:
# input_string = "babad"
# print(f"Longest palindromic substring: {longest_palindromic_substring(input_string)}")
#==============================================================================================================================================

# def longest_palindromic_substring(s):
#     if len(s) == "":
#         return ""

#     def expand_around_center(s, left, right):
#         while( left >= 0 and right < len(s) and s[left] == s[right]):
#             left = left -1
#             right = right + 1
#         return s[left + 1: right]

#     longest = ""
#     for i in range(len(s)):
#         temp = expand_around_center(s,i,i)
#         if len(temp) > len(longest):
#             longest = temp

#         temp = expand_around_center(s, i, i+1)
#         if len(temp) > len(longest):
#             longest = temp
        
#     return longest
# input_string = "peeneeyabcdefgehigigih"#"babad"

# print(f"Longest palindromic substring : {longest_palindromic_substring(input_string)}")
#==================================================================================================================================================

# def is_palindrome(s):
#     cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
#     #print(cleaned_string)
#     left, right = 0, len(cleaned_string)-1

#     while left < right:
#         if cleaned_string[left] != cleaned_string[right]:
#             return False
#         left = left + 1
#         right = right - 1
    
#     return True

# # Example usage:
# print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
# print(is_palindrome("racecar"))  # Output: True
# print(is_palindrome("hello"))  # Output: False

#=================================================================================================================================================

# def merge_intervals(intervals):
#     intervals.sort(key=lambda x: x[0])
#     merged = []

#     for interval in intervals:
#         # If the merged list is empty or the current interval doesn't overlap with the previous one, add it to the merged list
#         print(f"Interval",interval[0])
#         if not merged or merged[-1][1] < interval[0]:
#             merged.append(interval)
#         else:
#             # If it does overlap, merge the current interval with the last interval in merged list
#             merged[-1][1] = max(merged[-1][1], interval[1])

#     return merged

# # Example usage:
# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# merged_intervals = merge_intervals(intervals)
# print(merged_intervals)

#=================================================================================================================================================
# def merge_intervals(intervals):
#     intervals.sort(key=lambda x:x[0])
#     merge = []
#     for interval in intervals:
#         if not merge or merge[-1][1] < interval[0]:
#             merge.append(interval)
#         else:
#             merge[-1][1] = max(merge[-1][1], interval[1])
    
#     return merge

# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# #intervals = [[1,3], [2,5], [4,10], [9,16], [18,20]]
# print(f"{merge_intervals(intervals)}")

#=================================================================================================================================================
# def find_majority_element(nums):
#     count = 0
#     candidate = None
#     for num in nums:
#         if count == 0:
#             candidate = num
#         else:
#             count += 1 if num == candidate else -1
    
#     if nums.count(candidate) > (len(nums) // 2):
#         return candidate
#     else:
#         None

# # Example usage:
# nums = [2, 2, 1, 1, 1, 2, 2, 1, 1]
# majority_element = find_majority_element(nums)
# print(f"Majority element is: {majority_element}")
#=================================================================================================================================================
# Binary Search Implementation*: Write a function to implement binary search in a sorted array

# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1

#     while left < right :
#         mid = (left + right)//2

#         if arr[mid] == target:
#             return mid
        
#         if arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

# lst = [1,2,3,4,5,6,7,8,9,10]
# target = int(input(f"Enter the no to searched for in the list {lst}"))
# result = binary_search(lst, target)
# if result != -1 :
#     print("Target found")
# else:
#     print("Target not found")

#=================================================================================================================================================
# import heapq
# def find_kth_largest(nums, k):
#     # Step 1: Create a min-heap with the first k elements
#     min_heap = nums[:k]
#     heapq.heapify(min_heap)
    
#     # Step 2: Process the remaining elements
#     for num in nums[k:]:
#         if num > min_heap[0]:
#             heapq.heappop(min_heap)
#             heapq.heappush(min_heap, num)
    
#     # Step 3: The root of the heap is the Kth largest element
#     return min_heap[0]


# def find_kth(nums, k):
#     return find_kth_largest(nums,k)

# Example Usage
# array = [1,2,3,3,2,5,7,8]#[3, 2, 3, 1, 2, 4, 5, 5, 6] #[1, 2, 2, 3, 3, 4, 5, 5, 6]
# k = 6
# print(f"The {k}th largest element is: {find_kth(array, k)}")
#=================================================================================================================================================

# def kadane_algo(lst):
#     max_global = max_current = lst[0]

#     for i in range( 1, len(lst)):
#         max_current = max(lst[i], max_current + lst[i])
#         if max_current > max_global:
#             max_global = max_current

#     return max_global

# lst = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(f"kadane_algorithm : max value of subarray : {kadane_algo(lst)}")

#==================================================================================================================================
# s = "hello"
# def str_rev(strs):
#     temp = ""
#     i = len(strs) -1
#     while i >= 0:
#         temp = temp + strs[i]
#         i = i - 1
#     return temp

# print(str_rev("Hello"))

# def reverse_sentence(sentence):
#     words = sentence.split()
#     rev_words = words[::-1]
#     print(rev_words)
#     return " ".join(rev_words)

# print(reverse_sentence("hello World"))
#==================================================================================================================================
# from itertools import permutations

# string = "ABC"
# for i in permutations(string):
#     print("".join(i))

# #==================================================================================================================================
# def permute_string(string):
#     if len(string) == 1:
#         return [string]
    
#     permutations = []

#     for i in range(len(string)):
#         remaining_chars = string[:i] + string[i+1:]
#         for p in permute_string(remaining_chars):
#             permutations.append(string[i] + p)
    
#     return permutations

# perm_string = "ABCD"
# print(permute_string(perm_string))
#==================================================================================================================================

# def evaluate_rpn(tokens):
#     stack = []
#     for token in tokens:
#         if token in "+-*/":
#             # Pop the last two operands from the stack
#             b = stack.pop()
#             a = stack.pop()
#             if token == "+":
#                 stack.append(a + b)
#             elif token == "-":
#                 stack.append(a - b)
#             elif token == "*":
#                 stack.append(a * b)
#             elif token == "/":
#                 # Perform integer division
#                 stack.append(int(a / b))
#         else:
#             # Push the operand to the stack
#             stack.append(int(token))
#     return stack[0]

# # Example usage
# tokens = ["2", "1", "+", "3", "*"]  # Equivalent to (2 + 1) * 3
# result = evaluate_rpn(tokens)
# print(result)  # Output will be 9
#==================================================================================================================================
# class Node:
#     def __init__(self, data):
#         self.data = data  # The value stored in the node
#         self.next = None  # Pointer to the next node

# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None  # Initialize the head of the list as None

#     # Insert at the beginning
#     def insert_at_beginning(self, data):
#         new_node = Node(data)
#         new_node.next = self.head  # New node points to the old head
#         self.head = new_node  # The head now points to the new node

#     # Insert at the end
#     def insert_at_end(self, data):
#         new_node = Node(data)
#         if self.head is None:  # If the list is empty
#             self.head = new_node
#             return
#         last = self.head
#         while last.next:  # Traverse to the end of the list
#             last = last.next
#         last.next = new_node  # Point the last node to the new node

#     # Delete a node by value
#     def delete_node(self, key):
#         temp = self.head
#         # If the node to be deleted is the head
#         if temp is not None:
#             if temp.data == key:
#                 self.head = temp.next  # Change head
#                 temp = None  # Free memory
#                 return
#         # Traverse to find the node to be deleted
#         while temp is not None:
#             if temp.data == key:
#                 break
#             prev = temp
#             temp = temp.next
#         # If the key is not present in the list
#         if temp == None:
#             return
#         # Unlink the node from the list
#         prev.next = temp.next
#         temp = None  # Free memory

#     # Search for a node by value
#     def search(self, key):
#         current = self.head
#         while current:  # Traverse through the list
#             if current.data == key:
#                 return True  # Key found
#             current = current.next
#         return False  # Key not found

#     # Display the linked list
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")



# # Create a linked list
# llist = SinglyLinkedList()

# # Insert elements
# llist.insert_at_end(10)
# llist.insert_at_end(20)
# llist.insert_at_beginning(5)
# llist.insert_at_end(30)

# # Display the list
# llist.display()  # Output: 5 -> 10 -> 20 -> 30 -> None

# # Delete a node
# llist.delete_node(20)

# # Display the list after deletion
# llist.display()  # Output: 5 -> 10 -> 30 -> None

# # Search for a node
# print(llist.search(10))  # Output: True
# print(llist.search(20))  # Output: False
#==================================================================================================================================
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_at_beginning(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
    
#     def insert_at_end(self, data):
#         new_node = Node(data)
        
#         if self.head == None:
#             self.head = new_node
#             return

#         cur = self.head
#         while cur.next:
#             cur = cur.next

#         cur.next = new_node
    
#     def display_list(self):
#         if self.head == None:
#             print("The list is empty")
#         else:
#             print("The linked list :")
#             temp = self.head
#             while temp != None:
#                 print(temp.data, end = " -> ")
#                 temp = temp.next
        
#         print("None")

#     def delete_item(self, key):
#         temp = self.head

#         if temp is not None:
#             if temp.data == key:
#                 self.head = temp.next
#                 temp = None
#                 return
        
#         while temp != None:
#             if temp.data == key:
#                 break
#             prev = temp
#             temp = temp.next

#         if temp == None:
#             return

#         prev.next = temp.next
#         temp = None

#     def search_list(self, key):
#         temp = self.head
#         while temp != None:
#             if temp.data == key:
#                 return True
#             temp = temp.next
#         return False

#     def make_loop_at_end(self):
#         temp = self.head
#         store = None
#         while temp.next != None:
#             if temp.data == 20:
#                 store = temp
#             temp = temp.next

#         temp.next = store

#     def find_loop(self):
#         fast = self.head
#         slow = self.head

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
            
#             if slow == fast:
#                 return True

#         return False
    
#     def find_and_remove_loop(self):
#         fast = self.head
#         slow = self.head

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#             if slow == fast:
#                 break
#         else:
#             return False

#         slow = self.head
#         while slow != fast:
#             slow = slow.next
#             fast = fast.next

#         while fast.next != slow: 
#             fast = fast.next
#         fast.next = None

#         return True


# llist = LinkedList()
# llist.insert_at_beginning(10)
# llist.insert_at_beginning(20)
# llist.insert_at_beginning(30)
# llist.insert_at_beginning(40)
# llist.insert_at_beginning(50)
# llist.insert_at_end(80)
# llist.insert_at_end(90)
# item_to_be_searched = 100
# if llist.search_list(item_to_be_searched):
#     print(f"Searched item {item_to_be_searched} found")
# else:
#     print("Item dint found")
# llist.display_list()
# llist.delete_item(50)
# llist.display_list()
# llist.make_loop_at_end()

# print(f"Loop found in list : {llist.find_loop()}")
# llist.find_and_remove_loop()
# llist.display_list()

#==================================================================================================================================

# def first_non_repeating_char(string):
#     frequency = {}

#     for char in string:
#         if char not in frequency:
#             frequency[char] = 1
#         else:
#             frequency[char] += 1

#     for char in string:
#         if frequency[char] == 1:
#             return char

#     return None

# string = "swisswatich"
# result = first_non_repeating_char(string)
# print(f"The first non-repeating character is: {result}")
#==================================================================================================================================

#==================================================================================================================================
# def generate_powerset(s):
#     power_set = [[]]

#     for elem in s:
#         power_set += [subset + [elem] for subset in power_set]

#     return power_set

# s = [1,2,3]
# result = generate_powerset(s)

# for i in result:
#     print(i)
#=====================================================================================================================================

# from collections import Counter
# import heapq

# def top_k_frequent(nums, k):
#     freq = Counter(nums)
    
#         # Step 2: Use a heap to store the k most frequent elements
#         # The heap stores elements as (frequency, element), and by default heapq creates a min-heap
#         # We use negative frequency to simulate a max-heap
#     heap = []
#     for key, value in freq.items():
#         heapq.heappush(heap, (-value, key))
    
#     # Step 3: Extract the top k frequent elements from the heap
#     result = []
#     for _ in range(k):
#         result.append(heapq.heappop(heap)[1])
    
#     return result

# # Example usage
# nums = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4]
# k = 2
# print(top_k_frequent(nums, k))  # Output: [3, 1]

#=====================================================================================================================================

# from collections import Counter
# import heapq

# def top_k_frequent(nums, k):
#     freq = Counter(nums)

#     heap = []
#     for key, value in freq.items():
#         heapq.heappush(heap, (-value, key))

#     k_list = []
#     for i in range(k):
#         k_list.append(heapq.heappop(heap)[1])

#     return k_list

# nums = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4]
# k = 2
# print(top_k_frequent(nums, k))

#=====================================================================================================================================
# from collections import Counter
# import heapq
# def top_k_frequent(arr,k):
#     freq = Counter(arr)

#     heap = []

#     for key, value in freq.items():
#         heapq.heappush(heap, (-value, key))
    
#     print(heap)
    
#     result = []
#     for i in range(k):
#         result.append(heapq.heappop(heap)[1])
    
#     print(result)
#     return result

# arr = [1,1,2,2,2,3,3,3,3,4,6,7,2,3,3,1]
# k = 4
# print(top_k_frequent(arr,k))
#=====================================================================================================================================

# from collections import OrderedDict

# class LRUCache:
#     def __init__(self, capacity: int):
#         self.cache = OrderedDict()
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         else:
#             # Move the accessed item to the end to show that it was recently used
#             self.cache.move_to_end(key)
#             return self.cache[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             # Update the value
#             self.cache.move_to_end(key)
#         elif len(self.cache) >= self.capacity:
#             # Remove the first item (least recently used)
#             self.cache.popitem(last=False)
        
#         # Insert the item into the cache
#         self.cache[key] = value

# # Example usage:
# lru_cache = LRUCache(2)  # Cache capacity of 2
# lru_cache.put(1, 1)
# lru_cache.put(2, 2)
# print(lru_cache.get(1))  # Returns 1
# lru_cache.put(3, 3)      # Evicts key 2
# print(lru_cache.get(2))  # Returns -1 (not found)
# lru_cache.put(4, 4)      # Evicts key 1
# print(lru_cache.get(1))  # Returns -1 (not found)
# print(lru_cache.get(3))  # Returns 3
# print(lru_cache.get(4))  # Returns 4
#=====================================================================================================================================
# def exist(board, word):
#     rows, cols = len(board), len(board[0])
    
#     def dfs(r, c, index):
#         if index == len(word):
#             return True
#         if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
#             return False
        
#         # Mark the cell as visited
#         temp = board[r][c]
#         board[r][c] = "#"
        
#         # Explore the four directions
#         found = (dfs(r + 1, c, index + 1) or 
#                  dfs(r - 1, c, index + 1) or 
#                  dfs(r, c + 1, index + 1) or 
#                  dfs(r, c - 1, index + 1))
        
#         # Backtrack
#         board[r][c] = temp
#         return found
    
#     for i in range(rows):
#         for j in range(cols):
#             if dfs(i, j, 0):
#                 return True
#     return False

# # Example usage:
# board = [
#     ['A', 'B', 'C', 'E'],
#     ['S', 'F', 'C', 'S'],
#     ['A', 'D', 'E', 'E']
# ]
# word = "CCES"
# print(exist(board, word))  # Output: True
#=====================================================================================================================================
# def count_inversions(arr):
#     count = 0
#     n = len(arr)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if arr[i] > arr[j]:
#                 count += 1
#     return count

# arr = [8, 4, 2, 1]
# print(f"Number of inversions: {count_inversions(arr)}")

#=====================================================================================================================================

# def inversion(arr):
#     count = 0
#     n = len(arr)

#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[i] > arr[j]:
#                 count += 1
    
#     return count

# arr = [8,4,2,1]
# print(f"Calculate the inversion : {inversion(arr)}")

#=====================================================================================================================================
# def decorator_func(fun):
#     def wrapper(*args, **kwargs):
#         print(f"The function {fun.__name__} and its args :{args} and kwargs : {kwargs}")
#         result = fun(*args, **kwargs)
#         print(f"The function {fun.__name__} and the result is : {result}")
#         return result
#     return wrapper

# @decorator_func
# def add(a, b):
#     return a+b

# result = add(a=2, b=3)
# print(result)
#=====================================================================================================================================
# def check_prime(num):
#     if num < 2:
#         return False
    
#     for i in range(2, int((num**0.5) + 1)):
#         if num % i == 0:
#             return False

#     return True

# def gen_prime():
#     num = 2
#     while True:
#         if check_prime(num):
#             yield num
#         num = num + 1

# prime = gen_prime()
# for i in range(12):
#     print(next(prime))
#=====================================================================================================================================

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# class BinaryTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, value):
#         """Insert a new node with the given value into the binary tree."""
#         new_node = Node(value)
#         if self.root is None:
#             self.root = new_node
#         else:
#             self._insert_recursive(self.root, new_node)

#     def _insert_recursive(self, current, new_node):
#         """Helper method to recursively insert a new node into the tree."""
#         if new_node.value < current.value:
#             if current.left is None:
#                 current.left = new_node
#             else:
#                 self._insert_recursive(current.left, new_node)
#         else:
#             if current.right is None:
#                 current.right = new_node
#             else:
#                 self._insert_recursive(current.right, new_node)

#     def in_order_traversal(self, node, result=None):
#         """Perform an in-order traversal of the tree."""
#         if result is None:
#             result = []
#         if node:
#             self.in_order_traversal(node.left, result)
#             result.append(node.value)
#             self.in_order_traversal(node.right, result)
#         return result

#     def pre_order_traversal(self, node, result=None):
#         """Perform a pre-order traversal of the tree."""
#         if result is None:
#             result = []
#         if node:
#             result.append(node.value)
#             self.pre_order_traversal(node.left, result)
#             self.pre_order_traversal(node.right, result)
#         return result

#     def post_order_traversal(self, node, result=None):
#         """Perform a post-order traversal of the tree."""
#         if result is None:
#             result = []
#         if node:
#             self.post_order_traversal(node.left, result)
#             self.post_order_traversal(node.right, result)
#             result.append(node.value)
#         return result

#     def height(self, node):
#         """Calculate the height of the tree."""
#         if node is None:
#             return -1
#         left_height = self.height(node.left)
#         right_height = self.height(node.right)
#         return max(left_height, right_height) + 1

# # Example Usage
# if __name__ == "__main__":
#     bt = BinaryTree()
#     bt.insert(5)
#     bt.insert(3)
#     bt.insert(7)
#     bt.insert(2)
#     bt.insert(4)
#     bt.insert(6)
#     bt.insert(8)

#     print("In-order Traversal:", bt.in_order_traversal(bt.root))
#     print("Pre-order Traversal:", bt.pre_order_traversal(bt.root))
#     print("Post-order Traversal:", bt.post_order_traversal(bt.root))
#     print("Height of the tree:", bt.height(bt.root))

#=====================================================================================================================================

# from collections import deque

# def word_ladder(start_word, end_word, word_dict):
#     # Initialize the queue for BFS with the start word and path length of 1
#     queue = deque([(start_word, 1)])
    
#     # Convert word list to set for faster lookup
#     word_dict = set(word_dict)
    
#     # Remove the start word from the dictionary if it's present
#     if start_word in word_dict:
#         word_dict.remove(start_word)
    
#     while queue:
#         current_word, path_length = queue.popleft()
        
#         # Try all possible single letter transformations
#         for i in range(len(current_word)):
#             for char in 'abcdefghijklmnopqrstuvwxyz':
#                 if char != current_word[i]:  # Only consider different characters
#                     next_word = current_word[:i] + char + current_word[i+1:]
                    
#                     # If the transformed word is the end word
#                     if next_word == end_word:
#                         return path_length + 1
                    
#                     # If the transformed word is in the dictionary and hasn't been visited
#                     if next_word in word_dict:
#                         word_dict.remove(next_word)  # Mark as visited
#                         queue.append((next_word, path_length + 1))
    
#     return 0  # No transformation sequence found

# # Example Usage
# start = "hit"
# end = "cog"
# dictionary = ["hot", "dot", "dog", "lot", "log", "cog"]

# result = word_ladder(start, end, dictionary)
# print(f"Shortest transformation sequence length from '{start}' to '{end}': {result}")

#=====================================================================================================================================

# array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# def kadane(arr):
#     max_cur = max_global = arr[0]

#     for i in range(1, len(arr)):
#         max_cur = max(arr[i], max_cur + arr[i])
#         if max_cur > max_global:
#             max_global = max_cur

#     return max_global

# print(kadane(array))
#=====================================================================================================================================

# matrix = [[1,2,3,4],
#           [5,6,7,8],
#           [9,10,11,12]
#           ]

# rows = len(matrix)
# cols = len(matrix[0])
# transposed_matrix = []

# for i in range(cols):
#     new_row=[]
#     for j in range(rows):
#         new_row.append(matrix[j][i])
#     transposed_matrix.append(new_row)

# for row in transposed_matrix:
#     print(row)

#=====================================================================================================================================

#Shallow copy example

# A shallow copy creates a new object but inserts references into it to the objects found in the original. 
# If the original object contains the other objects(like lists within list)then shallow copy will reference
# the same objects not new copies of those objects.
# import copy
# original_list = [1,2, [3, 4]]
# shallow_copied_list = copy.copy(original_list)
# print("Shallow Copy Example")
# print("Original list : ", original_list)
# print("shallow copied list : ", shallow_copied_list)

# shallow_copied_list[2][0] = 99
# shallow_copied_list[1] = 555
# print("Original list : ", original_list)
# print("shallow copied list : ", shallow_copied_list)


# #Deep copy example

# # Deep copy creates a new object and recurssively copies all the object found in the original object. 
# # New object is entirely independent of the original object. 

# import copy
# original_list1 = [1,2, [3, 4]]
# shallow_copied_list1 = copy.deepcopy(original_list1)
# print("Deep Copy Example")
# print("Original list1 : ", original_list1)
# print("shallow copied list1 : ", shallow_copied_list1)

# shallow_copied_list1[2][0] = 99

# print("Original list1 : ", original_list1)
# print("shallow copied list1 : ", shallow_copied_list1)

#=====================================================================================================================================
# lst = [2,1,3,5,7,6,5]
# newlist = sorted(lst)
# print(newlist)
# lst.sort(key=None)
# print(lst)

# words = ["picnic", "cat", "cherry", "cache", "color","wonderlaw"]
# newwords = sorted(words)#, key=len)
# print(newwords)

# data = [(1, 'cherry'), (2,'banana'), (3, 'apple')]
# data.sort(key=lambda x:x[1])
# print(data)

# students = [
#     {'name': 'Sudarshan', 'age' : 36, 'grade' : 'A'},
#     {'name': 'Savitha', 'age': 34, 'grade': 'C'},
#     {'name': 'Ashwini', 'age': 31, 'grade': 'B'}
# ]

# students.sort(key=lambda x:x['name'])
# print(students)
# def sortbyage(students):
#     return students['age']

# sorted_students = sorted(students, key = sortbyage)
# sorted_students = sorted(students, key = lambda student :(student['grade'], student['age']))
# print(sorted_students)

#=====================================================================================================================================

# def binary_search(lst, target):
#     left = 0
#     right = len(lst) -1

#     while left < right:
#         mid = (left+right)//2
#         if lst[mid] == target:
#             return True
        
#         if lst[mid] < target:
#             left = mid +1
#         else:
#             right = mid - 1

#     return False


# lst = [1,2,3,4,5,6,7,8,9,10]
# target = 11
# result = binary_search(lst, target)
# if result == True:
#     print("Target found")
# else:
#     print("Target Not found")

#=====================================================================================================================================

# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
    
#     def display(self):
#         print(f"Car make : {self.make} and Model : {self.model}")

# class Car(Vehicle):
#     def __init__(self, make, model, doors):
#         super().__init__(make, model)
#         self.doors = doors

#     def display(self):
#         print(f"Car Make : {self.make}, Car Model : {self.model}, Car doors : {self.doors}")

# Hundai_car = Car('Hundai', 2023, 5)
# Hundai_car.display()

#=====================================================================================================================================
class Bird:
    def fly(self):
        print("Bird flies")

class sparrow(Bird):
    def fly(self):
        print("sparrow flies")

class ostrich(Bird):
    def fly(self):
        print("Ostrich cant fly")

def bird_flight(Bird):
    Bird.fly()

sparrow = sparrow()
ostrich = ostrich()

bird_flight(sparrow)
bird_flight(ostrich)

#=====================================================================================================================================

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            return amount
        else:
            print("Insufficient Funds")
            return amount
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def display(self):
        print(f"Bank Balance is : {self.__balance}")


sbAcc = BankAccount(100)
sbAcc.deposit(34)
sbAcc.display()
sbAcc.withdraw(20)
sbAcc.display()    
print(sbAcc.__balance)
















