# Course Link (under Section 5): https://nlbsg.udemy.com/course/the-complete-guide-to-mastering-modern-python/

# params with default values should be left to the end of thee function declaration to prevent errors
def greet(name : str, greeting : str = "Hello"):
    print(f'{greeting.capitalize()}, {name.capitalize()}!')

greet('Denver')
greet('Berlin', 'Ciao')
greet(greeting='So long', name='Dude') # when using positional args and specifying params, all args must be spelt out