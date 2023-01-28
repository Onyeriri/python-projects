print('Hello Anaconda')
num1 = 12
num2 = 5
num3 = 9.0

typeOf = type(num1)
typeOf1 = type(num3)

# basic type string
string1 = 'She\'s happy doing her chore\'s'
string2 = "Hello string"

# basic string manipulation
newString = "Hello:World:People".split(':')[2]
newString2 = "The total amount is " + str(6) + " dollars"
newString3 = "The number of egg " + str(5 + 4) + " remaining"

# basic boolean types operator
newBoolean = True is True
newBoolean1 = False is True
newBoolean2 = "This" == "This"
newBoolean3 = False is False

# dictionary
dog = {
    "name": 'Jack',
    "legs": 4,
    "height": 5,
    "number_of-Teeth": 7
}

# list
number_list = [1, 5, 4, 4]
number_list.pop()
number_list.sort()
number1 = number_list.copy()


# functions in python


def sum(a, b):
    return a + b


a = 0
while a <= 10:
    # print(f'{a}')
    a += 1

# birth_year = input('What\'s your birth year? ')
# current_year = 2023
# age = current_year - int(birth_year)

# building a counter
my_list = [1, 2, 4, 5];
total = 0;
counter = 0;

for item in my_list:
    counter += item

total = counter

image = [
    [0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0]
]

fill = '*'
empty = ' '


for item in image:
    for img in item:
        if img:
            print(fill, end='')
        else:
            print(empty, end='')
    print('')


new_range = list(range(1, 11))
# print(f"New range: {new_range}")
