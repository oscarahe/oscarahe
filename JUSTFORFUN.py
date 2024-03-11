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