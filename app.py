def add_two_values(num1, num2):
 try:
 if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
 raise TypeError("Both inputs must be numbers.")
 
 sum = num1 + num2
 return sum
 except TypeError as e:
 print(e)
