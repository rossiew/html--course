# Home work 
# task 1

# user=input("Enter a text: ")
# string=""
# for char in user:
#  string=char+string
# print("reversed string:",string)



# task 2

# def pcheck(word: str):  
#     iters = len(word)//2 
#     for i in range(iters): 
#         if word[i] != word[-i - 1]:  
#             return False  
#     return True  
 
# while True: 
#     word = input('Enter a word: ') 
#     print(f'{word} is palindrome' if pcheck() else 'not a palindrome')  
 




# task 3
# my_array = [1, 2, 3, 4, 5]

# start = 0
# end = len(my_array) - 1
# while start < end:
#     my_array[start], my_array[end] = my_array[end], my_array[start]
#     start += 1
#     end -= 1
# print("Reversed array:", my_array)


# word= input("enter a text: ")
# word="almaty"
# string=""
# for c in word:       #for-әрбір әріпті алып отырады
#     string=c+string
# print("reversed string:",string)


# Task {Find the largest number} with "for"
# numbers=[3,4,1,8,2]
# max_number=numbers[0]

# for number in numbers:
#     print(f"max_number({max_number})<number({number})?")
#     if max_number< number:
#         max_number=number
#     print(f"max_number = {max_number}")





# Task {Find the largest number} with "while"
# numbers=[3,4,1,8,2]
# max_number=numbers[0]
# i=1
# while i< len(numbers):
#     if max_number<numbers[i]:
#      max_number=numbers[i]
#     i+=1
# print(max_number)



# Home work {Fizz Buzz}
# for x in range (1,101):
#     if x %3==0 and x %5==0:
#         print("FizzBuzz")
#     elif x % 3==0:
#         print("Fizz")
#     elif x % 5==0:
#         print("Buzz")
#     else:
#         print(x)
 
# LESSON ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo


# total=0
# for x in range (1,31):
#     total= total+x
# print(total)




# for x in range (1,30):
#     if x % 2 ==1:
#         print(x*3)

# count=1
# while count<=10:
#     print(count)
#     count+=1




#кері айналдыру үшін
# count = 10
# while count<=1:
#     print(count)
#     count-=1  


#1 ,10  арасындағы сандарды қосу
# total=0
# count = 10
# while count>=1:
#     total+=count
#     count-=1 
#     print(total)



# 1, 30 арасындағы жұп сандар
# count=1
# while count<=30:
#     if count%2==0:
#       print(count)
#     count+=1



# 1, 30 арасындағы тақ санадар қосындысы
# total=0
# count=1
# while count<=30:
#      if count%2==1:
#       total+=count
#      count+=1
# print(total)



# with continue


# count=1
# while count<=30:
#      if count%2==1:
#        count+=1
#        continue
# print(count)
# count+=1




# break циклді қалаған жернен тоқтату үшін                 



# total = 0    
# count = 1
# while count <=100:
#     if count % 2 == 0:
#         total += 1
#     count +=1
# print(total)










# home work
# task 1
# for i in range(10, 21):
#     print(f" {i} = {i**2}")


# #task 2
# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1, n + 1):
#     sum += i
# print(f"{n} = {sum}")



# #task 3
# n = int(input("Enter a number n: "))
# sum = 1
# for i in range(1, n + 1):
#     sum *= i
# print(f"product number in 1 to {n} = {sum}")



# #task 4
# for x in range(20, 51):
#     if x % 3 == 0 and x % 5 != 0:
#         print(x)



# #task 5
# for x in range(35,88):
#  if x% 7==1  or x % 7==2 or x%7==5:
#   print(x)




# #task 6
# for x in range(1, 51):
#     if x % 5 == 0 or x % 7== 0:
#         print(x)



# #task 7
# for x in range (10,100):
#     if x%4==0 and x %6!=0:
#         print(x)



# #task 8
# total = 1
# for x in range(13, 100, 13):
#     if x % 2 != 0:
#         total *= x
# print(f"Произведение двузначных нечетных чисел, кратных 13, равно {total}")



# #task 9
# total = 0
# for x in range(100, 201):
#     if x % 17 == 0:
#         total += x
# print(f" {total}")


# #task 10

# n = int(input("Enter a number  N: "))
# sum = 0
# for x in range(1, n + 1):
#     sum += x ** 2
# print(f" {n} = {sum}")







#Lessooon
#Creating a string


summer='in sunny we go to the beach'
print(summer)
print(len(summer))