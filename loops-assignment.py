# Exercise 1
# Using the given list, print out a filtered version of the list with only the numbers that are less than ten

alist = [1,11,14,5,8,9]
new_alist = []
for i in alist:
    if i < 10:
        new_alist.append(i)
    else:
        continue
print(new_alist)    

# Exercise 2
# Merge and sort the two lists below
# Hint: You can use the .sort() method

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

l_1 += l_2
l_1.sort()

print(l_1)

# Exercise 3
# Square every number from 1 to 15

alist = []
i = 1
while i < 16:
    alist.append(i**2)

    i += 1
print(alist)



# Exercise 4
# Using List Comprehension and the given list, print out a filtered list with only the names that start with the letter 'a'. 
# The names in the outputted list should be title cased and have no whitespace.
# Hint: There is an empty string at the end of the list you will need to account for.

names_list = ['   amy', 'Briant', 'Ryan ', ' Alex', 'steve', '  ']
# expected output = ['Amy', 'Alex']
for char in names_list:
    char = char.strip().title()
    if char and char[0] == 'A':
        print(char)
 
# Exercise 5
# Print all Prime numbers from 1 to 100
# Hint: A Prime # is any # that is ONLY divisible by 1 and itself. 
# So think how you can iterate through the list of #s from 1 to 100 and check to see if its divisible by ANY # below it.

# The For/Each might be very helpful for this question. https://www.geeksforgeeks.org/using-else-conditional-statement-with-for-loop-in-python/
my_list= range(1,101)

for number in my_list:
    if number > 1:
        for i in range(2,number):
            if (number % i ==0):
                break
        else:
            print(number)


