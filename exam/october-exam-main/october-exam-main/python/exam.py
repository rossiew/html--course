## Strings

# Mandatory problems:


# String Concatenation:
# Concatenate the strings 'Python', 'is', 'a', 'powerful', 'language' to create a single string, 'Python is a powerful language.'


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



# String Formatting:
# Use f-strings to format the topic string in the following way: "Let's learn about {topic}."
topic='strings'
print( f"Let's learn about {topic}.")

# Substring Extraction:
# Extract and print the word 'Python' from the topic string.



## Bonus problems


# Substring Search:
# Check if the topic string contains the word 'Python' using the in keyword.

# String Replacement:
# Replace the word 'Python' in the topic string with 'programming' and print the modified string.

# String Splitting:
# Split the string 'Python,Java,C++,Ruby' into a list of programming languages using a comma as the separator.

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
programming_languages=['Python','Java','CSS','html']
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

# List Clearing:
# Use a method to clear all elements from the programming_languages list and print the empty list.

# List Index:
# Find and print the index of the element 'Java' in the programming_languages list.

# List Count:
# Count and print the number of times 'Python' appears in the programming_languages list.

# List Reversal:
# Reverse the order of elements in the programming_languages list and print the reversed list.


## Bonus problems


# List Copy:
# Create a new list languages_copy by copying the elements from the programming_languages list. Modify one element in the original list and ensure that the copy remains unchanged.

# List Slicing:
# Use slicing to create a new list first_two containing the first two elements from the programming_languages list.

# List Concatenation:
# Create a new list by concatenating the programming_languages list with another list containing ['Swift', 'Kotlin']. Print the resulting list.

# List Sorting:
# Sort the elements in the programming_languages list in reverse alphabetical order (descending) and print the sorted list.

# List Removal by Value:
# Remove all occurrences of 'JavaScript' from the programming_languages list and print the modified list.

# List Element Extraction:
# Use the pop() method to extract and print the last element of the programming_languages list, and then print the updated list without that element.

# List Element Counting:
# Count and print the total number of elements in the programming_languages list.

