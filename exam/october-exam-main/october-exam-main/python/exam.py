## Strings

# Mandatory problems:


# String Concatenation:
# Concatenate the strings 'Python', 'is', 'a', 'powerful', 'language' to create a single string, 'Python is a powerful language.'
# Define the strings
first = 'Python'
second = 'is'
third = 'a'
fourth = 'powerful'
fifth = 'language'


result = first + ' ' + second + ' ' + third + ' ' + fourth + ' ' + fifth + '.'
print(result)






# Variable Declaration:
# Declare a variable named topic and assign it the value "strings in Python."
topic="strings in python"
print(topic)



# Printing with Escape Symbols:
# Print the following sentence, including the double quotes: "Learning about "Python" strings is fun."
"Learning about Python strings is fun."
print('\"Learning about \"Python\" strings is fun.\"')



# String Length and Character Count:
# Calculate and print the length of the topic string. Also, count and print how many times the letter 's' appears in the string.
word = 'Learning about Python strings is fun'
print(len(word))
word = 'Learning about Python strings is fun'
print(word.count('s'))




# Uppercase and Lowercase Conversion:
# Create a new variable called upper_topic by converting the topic string to uppercase. Then, create another variable called lower_topic by converting the topic string to lowercase.


topic = "String"
upper_topic = topic.upper()
lower_topic = topic.lower()

print("Uppercase topic:", upper_topic)
print("Lowercase topic:", lower_topic)



# String Formatting:
# Use f-strings to format the topic string in the following way: "Let's learn about {topic}."
topic='strings'
print( f"Let's learn about {topic}.")




# Substring Extraction:
# Extract and print the word 'Python' from the topic string.

topic = "Python is a powerful language"
words = topic.split()
for word in words:
    if word == 'Python':
        print(word)







## Bonus problems


# Substring Search:
# Check if the topic string contains the word 'Python' using the in keyword.
topic = "Python is a powerful language"
if 'Python' in topic:
    print("yes")
else:
    print("no")






# String Replacement:
# Replace the word 'Python' in the topic string with 'programming' and print the modified string.
topic = "Python is a powerful language"
modified = topic.replace('Python', 'programming')
print(modified)





# String Splitting:
# Split the string 'Python,Java,C++,Ruby' into a list of programming languages using a comma as the separator.
languages_string = 'Python,Java,C++,Ruby'
languages_list = languages_string.split(',')
print(languages_list)





# Character at Index:
# Find and print the character at index 4 in the topic string.

# String Repetition:
# Create a new string that repeats the word 'Python' three times, separated by hyphens.

# Escape Symbols in String:
# Create a string that contains a newline character to print the following text on separate lines:
# Hello,
# World!

# String Capitalization:
# Capitalize the first letter of each word in the string 'python programming is amazing.'

# String Removal and Trimming:
# Remove any leading or trailing whitespace from the string '  Python For All ' and print the trimmed result.







## Lists

## Mandatory problems:


# List Append and Extend:
# Create a list called programming_languages with the elements ['Python', 'Java']. Use the append() method to add 'C++' to the list. Then, use the extend() method to add ['JavaScript', 'Ruby'] to the list. Print the updated list.
programming_languages=['Python','Java','Javascript','Ruby']
programming_languages.append('C++')
print(programming_languages)
programming_languages.extend('JavaScript')
programming_languages.extend('Ruby')
print(programming_languages)






# List Insertion:
# Insert the string 'C#' at the third position in the programming_languages list and print the modified list.
programming_languages.insert[3]
print(programming_languages)




# List Removal:
# Remove the second element from the programming_languages list and print the updated list.
programming_languages = ['Python', 'Java', 'Javascript', 'Ruby']
programming_languages.remove(1)
print(programming_languages)





# List Clearing:
# Use a method to clear all elements from the programming_languages list and print the empty list.
programming_languages = ['Python', 'Java', 'Javascript', 'Ruby']
programming_languages.clear()
print(programming_languages)



# List Index:
# Find and print the index of the element 'Java' in the programming_languages list.
programming_languages = ['Python', 'Java', 'Javascript', 'Ruby']
index_of_java = programming_languages.index('Java')
print( index_of_java)




# List Count:
# Count and print the number of times 'Python' appears in the programming_languages list.
programming_languages = ['Python', 'Java', 'Javascript', 'Ruby']
counter = programming_languages.count('Python')
print( counter)





# List Reversal:
# Reverse the order of elements in the programming_languages list and print the reversed list.
programming_languages = ['Python', 'Java', 'Javascript', 'Ruby']
programming_languages.reverse()
print(programming_languages)


## Bonus problems


# List Copy:
# Create a new list languages_copy by copying the elements from the programming_languages list. Modify one element in the original list and ensure that the copy remains unchanged.

programming_languages = ['Python', 'Java', 'Javascript', 'Ruby']
languages_copy = programming_languages.copy()
print("Original list:", programming_languages)
print("Copied list:", languages_copy)






# List Slicing:
# Use slicing to create a new list first_two containing the first two elements from the programming_languages list.

programming_languages = ['Python', 'Java', 'Javascript', 'Ruby']
first_two = programming_languages[:2]
print("The first two elements are:", first_two)




# List Concatenation:
# Create a new list by concatenating the programming_languages list with another list containing ['Swift', 'Kotlin']. Print the resulting list.





# List Sorting:
# Sort the elements in the programming_languages list in reverse alphabetical order (descending) and print the sorted list.
programming_languages = ['Python', 'Java', 'Javascript', 'Ruby']
programming_languages.sort()
print(programming_languages)




# List Removal by Value:
# Remove all occurrences of 'JavaScript' from the programming_languages list and print the modified list.
programming_languages = ['Python', 'Java', 'Javascript', 'Ruby']
del programming_languages[2]
print(programming_languages)



# List Element Extraction:
# Use the pop() method to extract and print the last element of the programming_languages list, and then print the updated list without that element.
programming_languages = ['Python', 'Java', 'Javascript', 'Ruby']

last_element = programming_languages.pop()
print("Last element:", last_element)
print("Updated:", programming_languages)



# List Element Counting:
# Count and print the total number of elements in the programming_languages list.

programming_languages = ['Python', 'Java', 'Javascript', 'Ruby']
total = len(programming_languages)
print("Total number of elements:", total)
