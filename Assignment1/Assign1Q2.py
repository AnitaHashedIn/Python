# 2.	Merge two lists as shown below
# Given I/P
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
#
#
# E/O
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

resList = []

for i in list1:
    for j in list2:
        resList += [i+" "+j]

print(resList)