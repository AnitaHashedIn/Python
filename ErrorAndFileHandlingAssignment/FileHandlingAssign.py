# Problem  – File Handling Exercise
#
# Write a python program to identify the longest words in a file, a.txt.

def longest_words(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]


print(longest_words('/Users/anitayadav/Documents/PythonAssignment/Python.txt'))