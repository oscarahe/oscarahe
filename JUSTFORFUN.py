 #Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
      new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
      aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")


#### nest a list inside a dictionary, more than one value be ac
#### asssociated with a single key in a dictionary loop through the dictionary,
###the value associated with each person would be a list of languages rather than a single language. Inside the dictionary’s for loop, we use another for loop

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

#This example shows one way to build a multiline string. 
#The first line assigns the first part of the message to the variable prompt.
#In the second line, the operator += takes the string that was assigned to prompt and adds the new string onto the end.
#The prompt now spans two lines, again with space after the question mark for clarity:

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

age = input("How old are you? ")
age=int(age)
age>=18

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

#While Loop

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message!= 'quit':
       print(message)



while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")   

#Functions
        
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

describe_pet('Gorda')

#Returning a dictionariy, a function can return any kind of value, the following
#function takes in parts of a name and returns a dictionary representing a person

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

####Accessing Indices and Values Safely with Built-in Function enumerate

numbers = [19, 3, 15, 7, 11]

print('\nCreating a bar chart from numbers:')
print(f'Index{"Value":>8}   Bar')

for index, value in enumerate(numbers):  # produces (index, value) tuples
    print(f'{index:>5}{value:>8}   {"*" * value}')