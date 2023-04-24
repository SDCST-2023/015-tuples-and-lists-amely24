#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
list=['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
print(list)
n1=str(input("enter the name from the list:"))
n2=str(input("enter a new name:"))
i=list.index(n1)
list.remove(n1)
list.insert(i, n2)

print(list)
print("\n")