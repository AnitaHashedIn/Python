# 3.	 Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look like the following list
# Given List:
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# Sub List to be added = ["h", "i", "j"]
# Expected output:
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list2  = ["h", "i", "j"]
list1[2][1][2].extend(list2)
print(list1)