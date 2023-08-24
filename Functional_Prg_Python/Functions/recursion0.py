# Course Link (under Section 5): https://nlbsg.udemy.com/course/the-complete-guide-to-mastering-modern-python/

def decrement_until_zero(n : int):
    print(n)

    # base case (to exit somehow)
    if n == 0:
        print('Program completed and n is now 0. Exitting!')
        return
    
    # recursive step
    decrement_until_zero(n - 1)

decrement_until_zero(10)