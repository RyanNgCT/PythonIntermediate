# To recap, the correct order for your parameters is:

#     Standard arguments
#     *args arguments
#     **kwargs arguments

def greet_w_age(*args : int, **kwargs):
    print(kwargs)
    print(args)

greet_w_age('Hello', 'there', name='Mario', age=10, gender='M')

# def greet_new(**kwargs, *args): # syntax error (Parameter cannot follow "**" parameter)
#     pass