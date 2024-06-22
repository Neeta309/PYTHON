#Armstrong numbers: is a number that is equal to the sum of its own digits each raised to the power of the number of digits

number = int(input("Enter the number: "))#Taking input as the integer
power = len(str(number))#Convert into string and then calculating the length by using the length function
temp = number #Assigning the original number to another variable so, that we can compare after doing manipulation in the temprory one that it's the
#same as the original one

ans = 0
while(temp > 0): # condition will be true upto the number is greater than 0
  r = temp % 10 # collecting the remainder in r
  ans = (r ** power) + ans # Calculating the exponential and then adding it to the answer 
  temp = temp // 10 #// are used to get the integer when we divide the number with 10
  
if int(number) == ans:#checking the number is armstrong or not.
  print("The number is amstrong number")
  
else:
  print("The number is not the armstrong number.")