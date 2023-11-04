
# # 1
# # Students = ["John","Jane","Sarah","Karl"]
# # print(Students[0] , Students[1])

# # Students[0]="Jannie"
# # print(Students[0])


# # Students[1]="Aibek"
# # print(Students[1])



# # study = ["Karl", "Jonn", "Lake"]
# # study.append("Mike")
# # print(study)



# # 2
# # thislist = ["Karl", "Zaen", "Ben"]
# # thislist.insert(1, "Mike")
# # print(thislist)

# # Subjects = ["math","english","phisics","chimestry"]
# # print (len(Subjects))--- [len] ----for all students show


# # grades=[4,5,3,4,3,5]
# # print(grades)

# # list1= [1, "Almaty", True]
# # print(list1)


# # temperatures=[12.5,22.0,38.9,19.5]
# # print(temperatures)
# # print(len(temperatures))



# # 3
# # cities=["Astana","Almaty","Aktau","Aktobe","Atrau"]
# # print(cities[2])
# # cities.append("Karaganda")
# # print(cities)

# # cities.insert(3, "Kostanay")
# # print(cities)


# # cities[3]="Pavlodar"
# # print(cities)



# # PART 1 of Home work


# # task {1}
# # a
# san=[]

# san.append(3)
# san.append(5)
# san.append(8)
# san.append(12)
# san.append(27)

# print(san)


# # b
# numbers=[]
# numbers.extend([1,2,3,4,5])
# print(numbers)




# # task {2}
# # a
# list=[2,4,8,12,47]
# san=sum(list)

# print(san)


# # b
# sum=0
# for num in numbers:
#    sum+=num
#    print(sum)

# # for yourself
# for num in numbers:
#     print(num)  #print(num*2)
   
   
   
#    # task {3}
# list = ["programmer", "file", "male", "microsoft", "time","lesson"]
# newlist = [x for x in list if len (x)>5]
# print(newlist)


# # b
# word_list = ["programmer", "file", "male", "microsoft", "time","lesson"]
# newlist=[]
# for word in word_list: #цикл
#   if len(word)>5:
#     newlist.append(word)
# print(newlist)


# #c advanced level
# newlist=[word for word in word_list if len(word)>5]
# print(word_list)
# print(newlist)


# # for yourself
# # import random
# # numbers=random.sample(range(10),5)---->massive if you need #sample- көп сан беруші
# # random_number=random.randit(0,10)-----> onlly 1 number if you need #randit-  бір сан беруші
# # print(random_number)

# # task{4}
# #a
# list = [17,2,9,4,10,5,43,13,147,32]
# list.sort()
# print(list)


# # b
# list=[87,103,93,13,169,42,467,2]
# list.sort(reverse=False)
# print(list)
# print(sorted(numbers))= new numbers



# # task{5}
# list=[1,3,2,4,5,7,6]
# list.remove(7)
# print(list)

# # b
# import random
# random_number=random.randit(0,10)


# # task{6}
# subject=['math','english','chimestry','biology']
# subject.reverse()
# print(subject)




# # task{7}
# a = "Microsoft"
# b = "Store"
# c = a + " " + b
# print(c)




# # task{8}
# list= (2,4,7,10,476,11,22,45,37,97)
# print(list[3:8])





# # task{9}
# list = ["proggrammer", "soul", "left", "profile", "cat","perfect"]
# newlist = []

# for x in list :
#   if "p" in x:
#     newlist.append(x)

# print(newlist)




# # task{10}
# element=(int(input("Enter a element:")))
# list=[1,2,3,4,5,6,7,8,9,10]
# if(element in list):
#     print("Element is found")
# else:
#     print("Element is not found")







# # PART2 of home work

# # task[1]
# list = [4,6,12,4,3,7,9,10]
# list[2] = 101

# print(list)



# # task [2]
# a
# mylist = ["work", "found", "view"]
# mylist.append("result")
# print(mylist)

# # b
# list=["line","story","space"]
# list.insert(1,"cloud")
# print(list)




# # task[4]
# thislist = ["apple", "banana", "cherry","mango","strawberry"]
# del thislist[0]
# print(thislist)





# # task[5]
# my_list = [1, 2, 3, 4, 5]

# for element in my_list:
#     print(element)




# # task[6]
# list = ["John","Ben","Patric","Jane"]
# list[2] = "Watson" 
# list[3] = "Benny"
# print(list)



# # task[7]
# list = [1, 2, 2, 3, 4, 4, 5,6,7,7]
# list2 = []
# for x in list:
#     if x not in list2:
#         list2.append(x)
# print(list2)




# # task[8]
# product=['milk','cheese','bread','cake','egg']
# product.reverse()
# print(product)



# # task[9]
# color=['red','blue','yellow','green','black',]
# color.clear()
# print(color)


# task[10]
# list1= "milk"
# list2="bread"

# print("a:", list2)
# print("b:", list1)



# Home work
# Task{1}
# import random
# numbers=random.sample(range(1,51),6)
# print(numbers)
# san=sum(numbers)
# print(san)

# # b
# avgerage = sum(numbers)/len(numbers)
# print("The average is ", avgerage)

# # c
# minimum = min(numbers); 
# print("The smallest number is:", minimum)

# # d
# maximum= max(numbers); 
# print("The largest number is:", maximum)

# # e
# polzovatel = input("Enter a number: ")
# if polzovatel==numbers:
#     print("Number is here!")
# else:
#     print("Number isn't here!")  



# task[2] Lottery Checker
# import random
# lottery_numbers=random.sample(range(1,51),6)
# user_numbers=[]
# for x in range(6):
#     user=int(input("Enter the number:  "))
#     user_numbers.append(user)
#     if x == lottery_numbers:
#         print("You are win!")
#     elif x >1:
#         print("You find one number!")

#     else:
#         print("You are not win.Try again")


# # task [3] To do List
# my_list = []


# task= input("Enter the task ")

# while list:
#     my_list.append(list)
#     list = input("Enter the task or leave it empty to finish)")


# print("Your list:")
# for list in my_list:
#     print(list)



# # task [4] Multiplication Table Generator


# number = int(input("Enter a number: "))
# print("Multiplication Table")
# for y in range(1,11):
#     result=number * y
#     print(f"{number}x{y}={result}")


# TODAY LESSON 05 .10. 2023

# number=int(input("enter a number:   "))
# if number >=1 and number <=  10 or number>= 20 and number<= 30:
#     print("hello")  
# elif number >=40 and number <=  50 or number>= 60 and number<= 70:
#     print("hi")


# month=input("Enter a month: ")
# if month =="june" or month=="july" or month=="august":
#     print("summer")
# elif month=="march" or month=="april" or month=="may":
#     print("spring")
# elif month=="september" or month=="octouber" or month=="november":
#     print("autumn")
# else:
#     print("winter")




# city=input("enter ur city: ")
# age=int(input("enter ur age:  "))
# if age >= 18  and (city== "almaty" or city=="shymkent"):
#     print("You are adult from  a large city")


















# Home work 


# #Task 1 {Even or odd cheker} 
# cheker=int(input("Enter a number: "))
# if cheker%2==0:
#     print(f"{cheker}  Even number ")    #f" -{cheker} = сөйлем арасында шығару  
# else:
#     print(f"{cheker}  Odd number")


    
    
    
# # Task 2 {Number Range Cheker}

# x = int(input("Enter a number between 0 and 100: "))
# if 0 <= x <= 100:
#     print(f"{x}  is in range")
# else:
#     print(f"{x}  is not range")





# # Task 3 {Simple Calculator}

# num1 = int (input("number 1: "))
# operator = input("operator: ")
# num2 = int(input("number 2: "))
# if operator == "+":
#     print(f"{num1} + {num2}={num1+num2}")

# elif  operator =="-":
#     print(f"{num1}-{num2}={num1-num2}")

# elif  operator == "*":
#     print(f"{num1} * {num2}= {num1*num2}")

# else:
#     print(f"{num1} / {num2}={num1/num2}")







# # Task 4 {Discount Calculator}
# price=float(input("Первоначальная цена? "))
# percent=float(input("Процент скидки? "))
# all=price-price*percent/100
# print(f"{all}  Ваша доп. цена  ")
# # print(f"{price} with {percent}% percent is {price*(1 - percent/100)}")




# # Task 5 {BMI Calculator}

# weight = int(input("Enter your weight in kilograms: "))
# height = float(input("Enter your height in meters: "))
# bmi = weight / height ** 2
# if bmi< 18.5:
#     print("Underweight")
# elif bmi >18.5 and bmi <  25:
#     print("Normal")
# else:
#  print("Overweight")




# Task 6 {Leap Year Cheker}
# year=int(input("Enter your year: "))
# if year%4==0:
#     print("Leap year")
# else:
#     print("Not leap year")


# #Task 7 {Quadratic Equation Solver} 





# # Task 8 {Number Guessing game}
# import random

# guessing = random.randint(1,100)
# user = int(input("Enter any number: "))
# while guessing!= user:
#     if user < guessing:
#         print("Too low")
#         user = int(input("Enter number again: "))
#     elif user > guessing:
#         print("Too high!")
#         user = int(input("Enter number again: "))
#     else:
#       break
# print("you usered it right!!")








# #10 {Persentage calculator} 




# print("Percentage Calculator")
# print("")

# x=float(input("Your Marks: "))
# percentage=100

# y=float(input("Total Marks: "))
# z=x*percentage / y

# print("You got=%.2f"%z)
# if z >=35:
#     print("Congratulation")
# else:
#     print("Try next time")




# Task 1 {prime number}

# num=int(input("Enter a number: "))
# if num>1:
#  print(num,"is a prime number")
#  for i  in range (2, num):
#    if (num%i)==0:
#     print(num,"is not a prime number")
# else:
#  print(num,"is a prime number")




# # Home work 
# # Task 1 {print numbers in range}
# number=[]
# for number in range(1, 11):
#  print(number)




# #  Task 2 {Sum of numbers in a range}

# sum = 0
# for number in range(1, 101):
#     sum += number
# print(f" The sum of numbers from 1 to 100 is : {sum}")





# # Task 3 {Even numbers in a range}

# for even_num in range(1, 21):
 # if even_num % 2 == 1:
  # print(even_num)





# # Task 4 {Table of a number}

# number=int(input("Enter a number: "))
# print(f"Multiplication table for {number}:")
# for x in range(1, 11):
#     result = number * x
#     print(f"{number} x {x} = {result}")





# # Task 5 {Countdown}
# for x in range(10, 0, -1):
#     print(x)



# lesson2




# text="hello world"
# for char in text:    #char- әрбір әріп үшін
#      print(char+char)




# count= 200
# while count>=100:
#  print(count)
# count-= 1    








