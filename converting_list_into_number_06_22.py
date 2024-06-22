#Creating a list of integers and then convert that elements into a single integer without converting it to string
# my_list = [1, 2, 3]  Not taking the hardcore values, we are taking the integers 


#Taking input for a list of integers from the user
input_string = input("Enter the elements of the list separated by space: ")
user_list = input_string.split()


power = len(my_list) - 1

digit = 0
for elements in my_list:
  digit = (elements*(10**power)) + digit
  power -= 1
  
print(digit)