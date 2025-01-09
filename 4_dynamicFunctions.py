# def check_3_digits(number):
#     return number in range (100,1000)

# result= check_3_digits(68)
# print(result)

# def check_3_digits(list1):
#     for n in list1:
#         if n in range(100,1000):
#             return True
#         else:
#             pass

# result=check_3_digits([55,99,6000])
# print(type(result))

# def check_3_digits(list1):
#     for n in list1:
#         if n in range(100,1000):
#             return True
#         else:
#             return False

# result= check_3_digits([100,400,600])
# print(result)


# def check_3_digits(list1):

#     three_digits_list=[]

#     for n in list1:
#         if n in range(100,1000):
#             three_digits_list.append(n)
#         else:
#             pass
#     return three_digits_list

# result= check_3_digits([555,99,600])
# print(result)

# coffee_prices=[('cappuccine', 1.5),
#                ('espresso', 1.2),
#                ('mocha', 1.9)]

# def most_expensive_coffee(list_of_prices):

#     highest_price= 0
#     my_most_expensive_coffee= ''

#     for coffee, price in list_of_prices:
#         if price> highest_price:
#             highest_price= price
#             my_most_expensive_coffee= coffee
#         else:
#             pass
#     return(my_most_expensive_coffee, highest_price)
# print(most_expensive_coffee(coffee_prices))



# coffee_prices=[('cappuccine', 1.5),
#                ('espresso', 1.2),
#                ('mocha', 1.9)]

# def most_expensive_coffee(list_of_prices):

#     highest_price= 0
#     my_most_expensive_coffee= ''

#     for coffee, price in list_of_prices:
#         if price> highest_price:
#             highest_price= price
#             my_most_expensive_coffee= coffee
#         else:
#             pass
#     return(my_most_expensive_coffee, highest_price)

# coffee, price= most_expensive_coffee(coffee_prices)
# print(f'the most expensive coffee is {coffee}, whose price is {price}')


# Dynamic Functions Practice #1--------------------------------------------------------------------------------------------------------
# Create a function (all_positives) that returns True if all the values in a list are positive,
# and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.



def positive_numbers(all_positives): #this is defining our function
    #it checks if all numbers are positive in a list
    #all_positives is the parameter in the function that would be called
    
    
    for n in all_positives: #a for loop that will iterate through each value in the list to see if conditions are met
        if n >= 0: #if a number in the list is 0 or greate, it would return true as it is a positive number
            return True
        else: #if a number in the list is less than 0, it would return False as all Nnumbers in the list have to be positive
             return False
        
result=positive_numbers([1,-6,9,11,-4])
 #if thee function was called, it list of numbers would be added in position of the all_positives parameter
print(result)
#would print True or False based on the values stored in a list 

# Dynamic Functions Practice #2-------------------------------------------------------------------------------------------------------
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000,
# and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.

def sum_less(num_list):    #This is defining the function 

    total = 0                   #Setting the total as 0 in the beginning
    for n in num_list:          #This is saying for each number in the list...
        if n in range (0,1000): #If it's within the range of 0-1000...
            total += n          #You add it to the total
        else:                   #And if the number isn't in the range...
            pass                #You pass it on moving to the next number
        
    #This loop repeats itself until there are no more numbers in the list
        
result2 = sum_less([55,100,200])  #The numbers inside the parentheses are the given values of num_list
print(result2) #This prints out the result
 
#Note for Mr.Evins: There's actually something weird with the code of the result being returned is none
#I'm assuming this is because somehow the numbers don't get added up
#But since they match the range that's why it displays that
#But it's almost time for us to go so we couldn't figure out the problem.
#Please help
        
# Dynamic Functions Practice #3--------------------------------------------------------------------------------------------------------
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers),
# and returns the result of said count.
            
number_list= [2,8,3,4,9]  #Is the list we are going to be suing for this example
even_nums= 0 #even_nums is a value that is set to 0 as there are no known values yet to be added 

def count_even(number_list):   #Defines the function 
    for n in number_list:      #For this number in the list
        if n%2==0:             #if the numbers remainder is 0,
            even_nums +1       #1 would be added to the variable even_nums as the number is even
        else:                  
            pass               #if a number is odd, the loop will pass through the value

result3= count_even(number_list)
print(result3)  #prints out the result

# Another additional note: This code also has the same problem as the one above it which is sad.
# Final Additional Note for Mr.Evins: The reason why there's varibales titled result, result2, and result 3 is so our code can work 
#Without the computer getting the variables mixed up and crashing out the program or something
