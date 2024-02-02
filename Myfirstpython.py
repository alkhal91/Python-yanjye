# list1=["a","b","c"]
# list2=[1,2,3]

# for x in list2:
#  list1.append(x)
# print(list1)

# fruits=("apple","banana","cherry","strowberry","rasberry")
# (green,yellow,*red)=fruits

# print(green)
# print(yellow)
# print(red)

# thisset = {"apple","banana","cherry"}
# print(thisset)

# import datetime
# x = datetime.datetime(2024,2,2)
# print(x.strftime("%c"))

# x = min(5, 10, 25)
# y = max(5, 10, 25)
# z = abs(-7.25)
# print(x)
# print(y)
# print(z)

# x = pow(4, 3)

# print(x)

# import math

# x=math.sqrt(64)
# print(x)

# x=math.ceil(1.4)
# y=math.floor(1.4)

# import json
# #someJSON:
# x= '{"name":"John","age":"30","city":"New York"}'

# #parse x:
# y = json.loads(x)

# #the result is Python dictionary:
# print(y["age"])

# try:
#   print("Hello")
# except:
#   print("Something went worng")
# else:
#   print("Nothing went worng")
# finally:
#   print("The 'try except' is finished")

# number=[1,2,3]
# number.append(5)
# print(number)

# for i in range(1,10):
#     if i == 3:
#         break
#     print(i)

# school_night = True
# if school_night == True:
#     print("No beer")
# else:
#     print("You may have beer")

# Lew_is_tired = False
# Lew_is_hungry = True
# if Lew_is_tired is True:
#     print("Lew has to teach")
# elif Lew_is_hungry is True:
#     print("No food for Lew")
# else:
#     print("Go on, have a biscuit")

def multiply_function(a, b):
    result = a * b
    result2 = result * result
    return result, result2

number_list = [1, 2, 3]
multiplier_list = [2, 4]
for n in number_list:
    print("_____________")
    for m in multiplier_list:
        current_answer, current_answer2 = multiply_function(n, m)
        print("The answer to %d * %d is :"%(n, m), current_answer)
        print("The result of this squared is :", current_answer2)