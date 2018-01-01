'''
This code raises a ZeroDivisionError exception for the following call: FancyDivide([0, 2, 4], 0)

Your task is to change the definition of SimpleDivide so that the call does not raise an exception. 
When dividing by 0, FancyDivide should return a list with all 0 elements. 
Any other error cases should still raise exceptions. 
You should only handle the ZeroDivisionError.
Your code must make use of the "ZeroDivisionError" keyword.
'''

def FancyDivide(list_of_numbers, index):
		denom = list_of_numbers[index]
		return [SimpleDivide(item, denom)
               for item in list_of_numbers]

# before
'''
def SimpleDivide(item, denom):
    
  	return item / denom
'''

def SimpleDivide(item, denom):
	try:
		t=item/denom
	except ZeroDivisionError:
		t=0
	return t

print(SimpleDivide(4,0))
# print(FancyDivide([0, 2, 4], 0))