#wap to create a function search(),in search function pass two parameters first,a list of ten nos and second,a number to search.if number is present in list return index of list otherwise return false.
def search(numbers,target):
 if target in numbers:
   return numbers.index(target)
 else:
   return False
numbers_list=[4,8,2,12,25,14,7,6,9,10]
number_to_find=99
result=search(numbers_list,number_to_find)
if result is not False:
 print(str(number_to_find)+"found at index"+str(result)+".")
else:
 print(str(number_to_find)+"not found in the list.")