#Program to check whether the given number is a buzz number or not:
#What is a buzz number: The number which is divisible by 7 or the last digit of the number is 7.

number = int(input("Enter the number: "))
if( number % 7 == 0 or number % 7 == 7):
  print(f"The {number} is a buzz number.")

else:
  print(f"The {number} is not a buzz number")