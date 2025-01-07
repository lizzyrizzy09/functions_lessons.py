# functions are ways to wrap your code into reuseable units


# how to define a function
# i only define the function once
# whatever I pass inside the parenthesis is called a parameter
# a parameter is a placeholder for future info
# def sayHello(name,age,month):
#     print(f"say hello{name}")
#     print(f"hello governor")
#     print(f"welcome back{name}")
#     print(f"your age is {age}")
#     print(f"your birth month is {month}")

# once you define a function you mustr call or invoke the function
# when i pass info into the called function, it is called an argument 
# sayHello("liz",15, "may")
# sayHello('jay', 22, "april")


# def determineElegibility(age):
#     #if your age is over 18, you can vote
#     #otherwise you can't
#     if age >= 18:
#         print("you can vote")
#     else:
#         print("you have to wait")

# determineElegibility(12)
# determineElegibility(15)
# determineElegibility(21)


# def willYouGraduate(gpa,credits,SAT):
#     #gpa: number float variable
#     #credits: number variable
#     #passed SAT: boolean

#     if (gpa >= 3.0) and (credits>=28) and (SAT== True):
#         print("you passed. good luck in college")
#     elif (gpa<3.0) or (credits< 28) or (SAT!= True):
#         print("back to the drawing board")
#     else:
#         print("talk to your counselor")
    

# willYouGraduate(2.8, 15, True)
# willYouGraduate(3.8, 28, True)
# willYouGraduate(3.5, 22, False)


#return= statement used to end a function and send result back to caller

# def add (x,y):
#     z= x + y
#     return z

# def subtract (x,y):
#     z= x - y
#     return z

# def multiply (x,y):
#     z= x * y
#     return z

# def divide (x,y):
#     z= x / y
#     return z

# print(add(1,2))
# print(subtract(1,2))
# print(multiply(1,2))
# print(divide(1,2))



def create_name(first, last):
    first= first.capitalize()
    last= last.capitalize()
    return first + " " + last

full_name= create_name( "lizzy", "rizzy")
print(full_name)