# From Notebooks to Modules
# Notebooks contains cells, which can contain either text or code.

# Python Modules

# Python modules are text files (.py) with the Pytho code

$ python hello_world.py
Hello, world!

# Running Python Modules

$ python circle.py
Circle with radius = 10
Area 98.6960440109

$ python
>>> import circle
Circle with radius = 10
Area 98.6960440109

# Python has a hidden variable __name__ to know if the code
# is being run or imported

$ python name.py
__main__

$ python
>>> import name 
name 

# An if statement can help us:
if __name__ == "__main__":
    #statements

# Running Python Modules: an example
# Running a module (__name__ is "__main__"):

$ python circle.py
Circle with radius = 10
Area 98.6960440109

# Importing a module (__name__ is a "name"), and we can runs its methods normally

$ python
>>> import circle
>>> circle.circle_area(10)
98.6960440109

# This is not debugging.py, but it works to show my knowledge in git. 

