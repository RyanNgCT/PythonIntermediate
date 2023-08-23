# Course Link (under Section 5): https://nlbsg.udemy.com/course/the-complete-guide-to-mastering-modern-python/

def greet(name : str): # using type hinting allows one to get context actions *specific to the datatype*
    name = name.capitalize()
    print(f'Hello, {name}!')


def do_something(): # also good convention to use snake_case.
    for i in range(3):
        print('Doing something')
    print('Done')

name = input('Enter your name: ')
try:
    greet(name)
except TypeError:
    print('Enter a valid name, please.')

do_something()
