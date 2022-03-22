
# create a class with name StringClass which should take string as an input from constructor. It should have method which should
# return the length of the string and a method to convert string to list of characters. This method will take an argument as
# string to convert.

# Solution

class StringClass :
    def __init__(self,string):
        self.string = string

    def StringLength(self):
        return len(self.string)

    def StringToList(self,str):
        return [int(i) for i in str]

StringObj = StringClass("12314532")
print("String Length: " + str(StringObj.StringLength()))
print("String to list: " + str(StringObj.StringToList("12314532")))

# Create class PairsPossible which should inherit from StringClass and should have a method for storing
# list of all possible pairs formed.
# It should also have a method to print list of every possible pair in same line but with space between them.
# Pairs should be in list.

#Solution

class PairsPossible(StringClass):
    def possible_pairs(self,list):
        res= [str(i)+" "+ str((i + 1) % len(list))
               for i in list]
        return res

PairsPoss = PairsPossible("12314532")
list = PairsPoss.StringToList("12314532")
res = PairsPoss.possible_pairs(list)
print("The pair list is : " + str(res))

