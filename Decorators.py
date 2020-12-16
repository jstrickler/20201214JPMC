#!/usr/bin/env python
# coding: utf-8

# # What are decorators?

# A decorator is a function (or class) that can modify another function (or class).

# ## Applying Decorators 

# The most important thing to learn about decorators is how they are applied.
# 
# When you say
# 
# ```python
# @my_decorator
# def my_function():
#     pass
# ```
# 
# it is *exactly* the same as saying
# 
# ```python
# my_function = my_decorator(my_function)
# ```
# 
# This takes care of the simple case where the decorator does not require arguments.
# 
# When a decorator needs arguments, it's slightly more complicated:
# 
# ```python
# @my_decorator(arg1, arg2, ...)
# def my_function():
#     pass
# ```
# 
# is the same as
# 
# ```python
# my_function = my_decorator(arg1, arg2, ...)(my_function)
# ```

# For a very simple case, we can make a decorator thst does some side effect, but doesn't really modify the target function.

# In[1]:


def bark(old_function):
    print("Woof! woof!")
    return old_function


# The decorator returns a *replacement function* that replaces the function you defined. In this case the replacement is really the orginal function.

# To apply, use the @ notation:

# In[3]:


@bark
def spam():
    print("Hello from spam()")


# Note that the output occurs when the output is applied, not when the subject function is run.
# 
# To make code that happens when the subject function is run, the decorator must define and return a new function, which in turns calls the original function. 

# In[10]:


from functools import wraps

def bark(old_function):
    
    @wraps(old_function)
    def replacement_function(*args, **kwargs):
        print("woof! woof!")  # EXTRA STUFF
        return
        old_return = old_function(*args, **kwargs)
        return old_return
    
    return replacement_function

@bark
def ham():
    print("hello from ham()")

# ham = bark(ham)

ham()
print(ham.__name__)


# In[ ]:




