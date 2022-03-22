# create a class with name StringClass which should take string as an input from constructor. It should have method which should
# return the length of the string and a method to convert string to list of characters. This method will take an argument as
# string to convert.
class StringClass :
    def __init__(self,string):
        self.string = string

    def StringLength(self):
        return len(self.string)

    def StringToList(self,str):
        return [i for i in str]

StringObj = StringClass("12314532")
print(StringObj.StringLength())
print(StringObj.StringToList("12314532"))