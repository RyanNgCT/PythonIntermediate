# Course Link (under Section 5): https://nlbsg.udemy.com/course/the-complete-guide-to-mastering-modern-python/

def greet_people(*people : str):
    print(people) # people is of type tuple
    for name in people:
        print('Hello', name)

greet_people('Mario', 'Luigi', 'Peach')

def greet_people(*people : str, greeting : str):
    for name in people:
        print(f'{greeting}, {name}!')

greet_people('Madrid', 'Oslo', 'Moscow', 'Helsinki', greeting="Hello") # need to specify greeting param


def do_something(**kwargs):
    if 'diet' in kwargs:
        del kwargs['diet']
    return kwargs # type dict

print(do_something(name="mario", color="red", diet="grass")) # params supplied must be in key=val format