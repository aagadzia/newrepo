
# coding: utf-8

# ###### @author: Amir Akbari
# 

# # Installing Python
# Please follow the instructions in **Windows_Installation.pdf**, **Mac_Installation.pdf**, and **Linux_Installation.pdf** to install Python version 3 via Anaconda, which is a distributor of Python. It provides Python Interpreter (engine), Sypder IDE (editor), Jupyter (notebook), ....
# 
# **Note**: Python does not always work well if the installation path (on your computer) contains Unicode characters, which might occur in a username. So, avoid naming your folders with special characters (or space in general). 
# While this isn’t an issue for installing Python or Anaconda, it is an issue for IPython which looks in
# `c:\user\username\.ipython` for configuration files. The solution is to define the HOME variable before launching
# IPython to a path that has only ASCII characters.

# # Understanding the Environment
# 
# Spyder is an IDE (Integrated Development Environment) for Python. The IDE makes it easier to code in Python and debug your code.
# 
# Spyder has three windows: 
#  
#  1. Editor: where you write your codes.
#     * your codes will have a *.py type
#     * in the editor, black font lines are your codes. 
#         * you can execute your whole code by choosing Run from the Run menu in the toolbar (top of the screen). Alternatively press F5 to run the code or press the GREEN TRIANGLE ICON.
#         * if you want to run one part of your code, create a cell by using #%%. Then use choose Run Cell from the Run menu. The SECOND green triangle or Ctrl+Enter does the same. This will execute the codes in the active cell, the one that your mouse has last clicked in. 
#     * In the $\color{green}\text{green}$ and $\color{gray}\text{gray}$ font lines are comments. These lines will not be executed. They help to document, add comments, and organize your code. 
#         * use # to comment out a line or use """ to open and close a few lines of comments.
#     * Tab completion - After entering 1 or more characters, pressing the tab button will bring up a list of functions, packages, and variables which match the typed text. 
#         * This will reduce the chance of a typo in the syntax
#         * If the list of matches is large, pressing tab again allows the arrow keys can be used to browse and select a completion.
#         * **Caution**: Python is whitespace sensitive. So indentation, either spaces or tabs, affects how Python interprets files. We will talk about these more later.
#         
#  2. IPython Console: where you run your code and see the outputs
#     * the output of your code will be shown here
#     * you can write part of your code and run only that part here
#     * you can use it as a scientific calculator, as well. 
#     
#  3. Source Window: it has three tabs
#     * VARIABLE EXPLORER: here you can see the variables you are using
#     * FILE EXPLORER: you can see all the files or folders in your working directory
#     * HELP: you can see help and documentation on the functions

# # Working with Python
# 
# Python is an interpreted high-level programming language for general-purpose programming. For finance related purposes, Python allows us to process data with complex formulas. It allows us to merge large tables and databases, moreover it helps us to run our analysis repeatedly on different databases.
# 
# * Python has an extensive set of functions (similar to those of MS-Excel), 
# * You can also work with more sophisticated  functions that others have written/developed, via importing those specific Python Libraries (_will talk about them shortly_).
# * You can  define your own functions as well.
# 
# Functions are called similar to MS-Excel: `FUNCTION_NAME( input_variables)`. For example, the `print` function, prints the value of the input in the IPython Console:

# In[2]:


print("Hello world!")


# More generally, functions can have multiple input variables and can generate multiple output variables. In general, the syntax is:
# 
# `out1, out2, out3, . . . = FUNCTION_NAME(in1, in2, in3, . . .)`.
# 
# In the example below, we are giving (parsing) 3 input variables to the `print` function:

# In[3]:


print("Hello", "to", "all!")


#  

# To access the help and documentation of each function, in the IPython console or in the Editor, select a function (double click on it) and press `Ctrl+I`. This will call the help on that function and show it in the Source window.
# 
# A Python program (aka `scripts`) is a collection of functions that can be run stand alone. For example, open a new file in the editor and type: ` print("Hello, World!")`. Then save the file as `hello.py` in the working directory. Then in the IPython Console type `%run hello.py`. This will call your script. This script will print "Hello, Word!", each time it is called. 

# In the IPython Console, type the following to call the script:

# In[4]:


get_ipython().run_line_magic('run', 'hello.py')


# # Variable Names and Types
# 
# Python, similar to MS-Excel, needs to know the type of the variables it is working with. Recall in MS-Excel, we can set the data type of each cell to  _Number, Date, Text, Currency, ..._. A similar setting exists in Python.
# 
# ## Data Names
# 
# In MS-Excel, each cell is a variable (e.g. `A2` or `B17`). In Python, we give a name to the variables we use (this can also be done in MS-Excel). Variable names can take many forms, although  
# 
# * they can only contain numbers, letters (both upper and lower), and underscores. 
# * Names must begin with a letter or an underscore. 
# * Names are `CaSe SeNsItIve`. That is, variables `A` and `a` are different variables.
# * Reserved Words:  The following names are Python keywords. They have special meaning and shouldn't be used as variable names:
# 
# 
# `as, or, in, is, if, and, del, not, try, for, def, from, elif, with, else, exec, pass, while, yield, break, print, class, raise, global, assert, except, import, lambda, return, continue, finally`
# 
# 
# If you define/use them in your code as a new variable, you'll get a syntax error.
# 
# Note: for readability, if you feel that you need to use one of these as a variable, you could use an underscore after it. For example, and_, class_, etc. That makes it different from the Python keyword.
# 
# As stated above, the following variable naming is not allowed either:
# 
# `
# x: = 1.0
# 
# 1X  = 1
# 
# X-1 = 1
# 
# for = 1`

# ## Data Types:
# 
# Some of the most commonly used variables are (_we will see the more complex ones later in the course_):
# 
# * Integer Numbers (aka INT): 
# 
# Integers are numbers starting from $1, 2, 3, ...,\infty$. For example:

# In[5]:


x = 40
print(x)


# **Caution**: Notice that large numbers never include commas. Compare these two
# examples. 
# 

# In[6]:


print(12345678)


# In[7]:


print(12,345,678)  


# In the second command, Python thinks that there are three numbers (i.e. 12, and 345, and 678) given to the `print` function, not one 8-digit number (i.e. 12345678).

# * Real Numbers (aka FLOAT)  
# 
# Real numbers are numbers with decimal values. e.g.,

# In[8]:


x = 40.0 
print(x)


# In[9]:


a = 13.56798
print(a)
print("%.2f" % a)   # if you want to display the data with 2 decimals
print(round(a,2))   # Alternatively you can round the data with 2 decimals


# * String (aka STR)
# 
# Strings are similar to the TEXT data type in MS-Excel., e.g.:

# In[10]:


x = "hello"
print(x)


# In order to make a string we may use a single quote sign `'` or double quotations `"`. Either works equally well. But if the string contains one, we need to use the other. For example

# In[11]:


x = "His name is Conan O'Brien"
print(x)


# In[12]:


x = 'My cat is named "Butters"'
print(x)


# If you need both a `'` and a `"` in your string, you can use the escape character \ which tells Python that the following character is to be taken as the literal character and is not a quote to delimit the string.  See it in action escaping the " below:

# In[13]:


x = "My cat's name is \"Butters\""
print(x) 


# * List (aka LIST), e.g.:
# ```
# List allows you to have a group of variables in one variable. For example,
# ```
# * * List of characters

# In[14]:


x = ['a','b','c'] 
print(x)


# * * List of numbers

# In[15]:


x = [1,5,23] 
print(x)


#   * * List of characters and numbers

# In[16]:


x = ['ball', 3.14, -50, 'university', "course"]
print(x)


#    * * List of strings

# In[17]:


x = ["’Twas brillig, and the slithy toves", 
     "Did gyre and gimble in the wabe:"] 
print(x)


#    * * List of Lists

# In[18]:


newEngland = [["Massachusetts",6692824],
              ["Connecticut",3596080],
              ["Maine",1328302],
              ["New Hampshire",1323459],
              ["Rhode Island",1051511],
              ["Vermont",626630]]
print(newEngland)


# * Boolean (aka BOOL), 
# 
# The Boolean variables are `0/1` or `True/False` variables. e.g.:

# In[19]:


x1 = True
y1 = False   


# Boolean variables are very useful in conditional statements, such as `IF` statements.

# ## Quick look at operations on Data Types
# ### Basic arithmetic operations on numbers
# * Basic operators:
#   * +, -, *, /: These add, subtraction, multiply, divide.
#   * **: This is for exponentiate (to the power).
#   * //: This is for integer divide (drops fractional part).
#   * %: This is to compute remainder on division for integers (MOD function in MS-Excel).

# In[20]:


a = 5
b = 2
x1 = a + b
x2 = a * b
x3 = a ** b
x4 = a / b
x5 = a // b
x6 = a % b

print(x1,x2,x3,x4,x5,x6)


# In[21]:


# The usual laws of arithmetic hold with respect to the priority of the operations
x7 = x1 + x2*x3**x4/x5
print(x7)


# $x_7 = x_1 + \frac{x_2 \; x_3^{x_4}}{x_5}$

# $\;\;\;\; = 7 + \frac{10 \; 25^{2.5}}{2}$

# $\;\;\;\; = 7 + \frac{10 \; 3125}{2}$

# $\;\;\;\; = 7 + 15625$

# $x_7 =  15632$

# ### working with strings
# You can simply add two strings together like this:

# In[22]:


First_Name = "Amir"
Last_Name  = "Akbari"
Full_Name = First_Name + " " + Last_Name
print(Full_Name)


# In[23]:


print("My name is",First_Name, Last_Name, "and I teach Financial Modeling.")    


# ### Working with Lists
# #### Accessing items of a list
# Consider the following example, where a list is called Alphabet:

# In[24]:


Alphabet = ["a","b","c","d","e","f"]


# To get the $i^{th}$ element of the list, we use the following syntax:`List_name[i-1]`. In Python, the index of a list (and array and matrix variables that we will see later) starts from 0. Example:
# 

# In[25]:


print ("The 1st item of Alphabet is: ", Alphabet[0]) 
print ("The 2nd item of Alphabet is: ", Alphabet[1]) 
print ("The Last item of Alphabet is: ", Alphabet[-1]) 


# This is equivalent to the `INDEX(array, row_num, [column_num])` function in MS-Excel, where you can access to a cell by give the row and column number of a cell to access it. For example, `INDEX(A4:C10, 2, 3)` returns cell `C5`.
# 
# 
# If you are interested in a few items, you can use a range

# In[26]:


print ("Items 2, 3, and 4 of Alphabet are: ", Alphabet[1:4]) # (Index 1,2,3 excluding 4)
print ("3 first items of Alphabet are: ", Alphabet[:3]) # (Index 0,1,2 excluding 3)
print ("Items 4 to end of Alphabet are: ", Alphabet[3:]) # (Index 3, 4, ...)


# If your variable is a list of list (like the newEngland example above):

# In[27]:


print("the first item of newEngland is:", newEngland[0])
print("and the first item of the first element of newEngland is:", newEngland[0][0])


#  if for any reason you want to access to an empty list:

# In[28]:


x = []
print(x)


# #### Functions of Lists
# * The `len()` function gives the length of a list variable (i.e. the number of items in the list). e.g.

# In[29]:


x = len(Alphabet)
print("Alphabet has", x, "items.")


# In MS-Excel, we can use the `COUNT()` function to get the length of an array of cells.
# 
# 
# 
# * One can insert an item in the List, at a certain place with the `.insert` feature, 
# * add an item to the end of the list with `.append` feature
# * If you want to remove an item from the list, use the `.remove` feature of the list:

# In[30]:


Alphabet.insert(2, 'Z') # add character `Z` as the 3rd item of Alphabet
Alphabet.append('B')    # add character `B` at the end of Alphabet
Alphabet.remove('f')    # remove character `f` from Alphabet

print(Alphabet)


# * If you are interested to find the index of an item of the list, use `.index` feature of the list:

# In[31]:


print(Alphabet)
Alphabet.index('c')


# Similarly in MS-Excel, we can use the `ROW()` and `COLUMN()` functions to get the row and column indexes of a cell.

# * You can easily sort a list by `.sort` feature:

# In[32]:


Alphabet.sort()
print("After sorting, Alphabet is:", Alphabet)


# In MS-Excel, we can use `Sort & Filter` option.

# In[33]:


# The sort feature works for numbers as well:
a = [1, -1, 40, 2.4, 0]
a.sort()
print(a)


# * Note that `.sort` permanently change the order of your list. If you want to keep the original ordering of the list but you need to sort it, say for just printing, you can use the `sorted()` function:

# In[34]:


numlist = [67, 54, 39, 47, 38, 23, 99, 91, 91, 70]
print("sorted numlist is:",sorted(numlist))
print("But numlist stays as-is:",numlist)


# * use `in` feature to check if an item  belongs to a list. 
# For example, running this statement will return `True`, because Alphabet includes "a".

# In[35]:


"a" in Alphabet  


# In[36]:


# And running this statement will return False
"r" in Alphabet                  


# #### Copying Lists
# 
# Lists are mutable and so assignment does not create a simple copy. After the assignment the changes to either variable affect both.

# In[37]:


x    = [1, 2, 3]
y    = x
y[0] = 10


print("y = ", y)
print("x = ", x)


# This is because of the memory management of Python. Setting `y = x`, also sets the memory pointer of `y` equal to that of the `x`. Therefore, if you change `y`, you are also changing `x`. This makes  data management more efficient by Python (but we don't care about it in this class). 
# 
# However, slicing a list creates a copy of the list and any immutable types in the list – but not mutable elements in the list. This helps you preserve the value of `x`. In this way, simply copy the content of `x` to `y`:

# In[38]:


x    = [1, 2, 3]
y    = x[:]
y[0] = 10
print("y = ",y)
print("x = ",x)


# ## Converting Variable Types
# Similar to MS-Excel. Sometimes variables are stored in a wrong format and we need to change them.
# 
# * You can find the type a variable `x` by entering:

# In[39]:


type(Alphabet)


# In[40]:


x1 = 40
type(x1)


# * convert a string (character) to a number 

# In[41]:


x2 = "30"
print("type of the variable x2 is", type(x2))
# Similarly
x3 = str(x1) 
print("type of the variable x3 is",type(x3))


# In MS-Excel, the function `TEXT()` does a similar job.

# * convert a number which is stored as a string (character) back to a number 

# In[42]:


x4 = int(x2) 
print("type of the variable x4 is",type(x4))


# In[43]:


x5 = float(x2) 
print("type of the variable x5 is",type(x5))


# Knowing the data type of the variables you are working with is important. For example since `x2` and `x3` are stored as a string (character) then `x2+x3` is '3040' (not 70)!

# In[44]:


print(x2+x3)


# however, `int(x2)+int(x3)` is 70.

# In[45]:


x = int(x2)+int(x3)
print(x)


# # IF statement
# 
# The concept of the `IF` statement is similar to the one in MS-Excel. There are three versions of the `IF` conditions: (1) if - then, (2)if-then-else, (3)if-then-elseif-then-else.
# 
# 
# In Python, the statement after the condition is considered the "then" statement of the `IF` statement and there is no need to include the  "then" argument. Simply add 4 spaces or 1 tab to open the "then" arguments.
#     
#  
# 1. Simple if-then statement: 
# 
# the syntax is as follows
#     
# `IF CONDITION :`
# 
# $\;\;\;\;$ `WHAT TO DO IF CONDITION HOLDS`
# 
# 
# For example:

# In[46]:


x = 5
if x > 0:
    print("x equals to", x)
    print("x is positive")


# 2. if- then- else
#     the syntax is as follows
#     
# `IF CONDITION :`
# 
# $\;\;\;\;$`WHAT TO DO IF CONDITION HOLDS`
# 
# `ELSE:`
# 
# $\;\;\;\;$`WHAT TO DO IF CONDITION DOES NOT HOLD`
# 
# For example:
#     

# In[47]:


y = 0   
if y > 0:
    print("y is positive")
else:
    print("y is not positive")


# 3. if- then- else if- then, ...
# 
# Nested if statement can be implemented with `elif` command (shorten version of else if). The syntax is as follows
#     
# `IF CONDITION_1 :`
# 
# $\;\;\;\;$`WHAT TO DO IF CONDITION_1 HOLDS`
# 
# `ELIF CONDITION_2 :`
# 
# $\;\;\;\;$`WHAT TO DO IF CONDITION_2 HOLDS`
# 
# `ELSE:`
# 
# $\;\;\;\;$`WHAT TO DO IF CONDITION_1 & CONDITION_2 DO NOT HOLD`
#     
# `elif` can be repeated as often as necessary. For example:    

# In[48]:


z = 0
if z > 0:
    print("z is positive")
elif z < 0:
    print("z is negative")
else:
    print("z must be 0")


# ## Logical Operators and Devices
# 
# Logical operators and devices are useful if you want to create (more complex) conditions. The core logical operators (besides `>` and `<`) are
# 
#   * `>=` :  Greater than or equal to
#   * `<=` :  Less than or equal to
#   * `==` :  Equal to
#   * `!=` :  Not equal to 
# 
# **Note:** Python uses `=` for assignment and `==` for testing equality. Whereas, in MS-Excel, you can use `=` in the `IF` statement for testing equality. There you can use `<>` to test for the `not equal` condition.  
# 
# 
# If you want to combine several conditions you use logical devices:
# 
# * `logical_and()`: Both logical expressions are True. Alternatively use `and` or `&` between conditions
# * `logical_or()` : Either of the logical expressions is True. Alternatively use `or ` between conditions 
# * `logical_not()`: Not True. Alternatively use `not` or `~` between conditions
# * `logical_xor()`: One expression True and One expression False. Alternatively use `^` between conditions
# 
# 
# There are three versions of all operators except XOR. 
# 1. the function (e.g. `logical_and()`) 
# 2. The keyword version (e.g. `and`),
# 3. the bitwise (e.g. `&`) 
# 
# The preferred method is the functional form. The keyword version can only be used with scalars (not arrays) and so it not useful when working with NumPy library (_to be discussed later_). Both the function and bitwise operators can be used with NumPy arrays, although care is required when using the bitwise operators. Bitwise operators have a high priority – higher than logical comparisons – and so parentheses are required around comparisons. For example, `(x>1) & (x<5)` is a valid statement, while `x>1 & x<5`, which is evaluated as `(x>(1 & x))<5`, produces an error.
# 
# There are equivalant logical operators in MS-Excel such as `AND()`, `OR()`, and `NOT()` functions that can be used in the `IF` statement.
# 
# 
# * Special case: for lists you can also use the `in` feature to check if an item  belongs to it. 

# In[49]:


Team = ['T','e','a','m']
if ~('i' in Team): 
    print('There is no "i" in "Team"!')


# You can achieve a similar functionality in MS-Excel too but it is less straight forward. You can use the `contain` search option in a column that is already `Filter`ed. 

# # For statement
# a `FOR` loop, allows you to iterate an operation for several times. There is no easy to access alternative in MS-Excel for loops. Often, people use an index variable (say row 1 to 10), and copy the equation in multiple rows in the adjacent  column to mimic the loop functionality.
# This is simplier in Python. The syntax is
# 
# `FOR CONDITION_1 :`
# 
# $\;\;\;\;$`WHAT TO DO IF CONDITION_1 HOLDS`
# 
# 
# For example, below, we ask Python to print "Financial Modeling is FUN with Python!"  10 times.
# We use the `RANGE` function to specify the number of iterations:

# In[50]:


# Example 1
for i in range(10):
    print("Financial Modeling is FUN with Python!" )


# The `RANGE(a,b,j)` function uses a start number `a`, a stop number `b` and a step size `j`. When not specified, `a=0` and `j=1`. For example, `range(10)` is equvalant of `range(0,10,1)` and `range(2,10)` is equvalant of `range(2,10,1)`.

# In[51]:


# Example 2
for i in range(2,10):
    print(i,end=' ') 
# the `end=' '` is used to avoid the enter at the end of each print.
# therefore the output is printed in one line:


# In[52]:


# Example 3
for ct in range(2,9,2):
    print(ct,end=' ')


# In[53]:


# Example 4
for ct in range(22,5,-3):
    print(ct,end=' ')


# Loops can also be defined over a list variable:

# In[54]:


# Example 5
for names in ["Sarah", "Ben","Moe"]:
    print(names)


# In[55]:


# a more advanced example of 5
CEOs = ['Bharat Masrani','David I. McKay','Lloyd Blankfein']

for i,company_name in enumerate(['TD','RBC','Goldman Sachs']):
    print('CEO of', company_name,'is',CEOs[i],'.' )
# here i gives the index of the loop for each iteration.


# Note that this is identical to:

# In[56]:


# a more advanced example of 5
Companies = ['TD','RBC','Goldman Sachs']
CEOs      = ['Bharat Masrani','David I. McKay','Lloyd Blankfein']

for i in range(len(Companies)):
    print('CEO of', Companies[i],'is',CEOs[i],'.' )
# here i gives the index of the loop for each iteration.


# The first, using the `enumerate`, allows us to write our code more readable.

# Loops can also be nested (a `FOR` loop inside another `FOR` loop). Pay attention to the spacing at the beginning  of each line, in each loose

# In[57]:


# Example 6
count = 0
x = range(10)
y = range(10)

for i in x:
    for j in y:
        count = count + j
print(count)


# **Important:** The iterable variable (in the above example `x` and `y`) should not be reassigned once inside the loop.

# A loop can be terminated early  using `break`. `break` is usually used after an `if` statement to terminate the
# loop prematurely if some condition has been met.

# In[58]:


# Example 7
x = range(10)
for i in x:
    print(i,end=' ')
    if i > 5:
        break


# # Define a Function:
# In Python, you can define your own function, in a separate file for example, and call it. This will help you with code-readability and debugging your code. You can test each function separately and then merge them all.
# 
# The syntax is as follows:
# 
# ` DEF FUNCTION_NAME(INPUT_VARIABLE):`
# 
# $\;\;\;\;$`PROCESS INPUT_VARIABLE`
# 
# $\;\;\;\;$`RETURN OUTPUT_VARIABLE (optional)`

# After defining your function, you should load it to Python. This way, Python learns about your newly defined function.
# Then you can parse any input variable you like to the function, as many times you like. 
# There are two ways to do so
# 1. Simple: copy the function you wrote in the console and run it. 
# 2. Complete: save it in a .py file (e.g. MyFunctions.py). Then load it similar to a library (see the next section)
#     

# _Example-1:_ 
# Write a function that accepts three numbers and calculates the product of them.

# In[59]:


def product_function(in1,in2,in3):
    product_all = in1 * in2 * in3
    return product_all


# In[60]:


# Run the function:
product_function(2,4,5)


# Now that we have this function, we can run the above function to get the product  of any 3 numbers we like. For example

# In[61]:


product_function(23,-4,5)


# _Example-2:_ 
# Print the name of the New England states with their population.  
# The name of the states and their population are given in the variable newEngland (above).
# Use a basic loop design pattern.

# In[62]:


newEngland = [["Massachusetts" , 6692824],
              ["Connecticut" , 3596080],
              ["Maine" , 1328302],
              ["New Hampshire" , 1323459],
              ["Rhode Island" , 1051511],
              ["Vermont" , 626630]]

# newEngland is a list of lists.
#   newEngland[i] is a list that stores the name state at row i and its population
#   newEngland[i][1] gives the first item, the name of the state i, 
#   newEngland[i][2] gives the second item of the list, here the population of the state i


# In[63]:


def print_state_info(state_data):
    print("Population          State")
    for i in range(0,len(state_data)):
        print(state_data[i][1], "        ", state_data[i][0])


# In[64]:


# Run the function:
print_state_info(newEngland)


# Now that we have this function, we can run the above function to get the information of any other region. For example, Mid Atlantic states:

# In[65]:


midAtlantic = [["New York",19746227],["New Jersey",8938175], ["Pennsylvania",12787209]]  
print_state_info(midAtlantic)


# _Example-3_: 
# Find the sum of the populations of the New England states. 
# The name of the states and their population are given in the variable newEngland.
# Print out how many states there are. 
# Use a basic loop design pattern.

# In[66]:


def population(state_data):
    """ Sums state populations """
    sum_       = 0
    num_states = len(state_data)
    for i in range(0,num_states):
        one_state = state_data[i]
        pop       = one_state[1]
        sum_      = sum_ + pop
    print("The total population of this list of states is",sum_)
    print("There are",num_states,"states in this list of states.")
# notice that I wanted to use the name SUM, but it is a reserved word. 
# I used an underscore after it, SUM_, to slightly modify the name, so Python does not get confused.# 


# In[67]:


# Run the function:
population(newEngland)


# In[68]:


population(midAtlantic)


# Furthermore, you can call a function inside another function. 

# # Libraries
# 
# In Python, many tools (functions) are not automatically loaded and are in modules called libraries. To be able to use the functions in a library, you first need to load the library. It is recommended to only load libraries that you need in each of your code. In this way, you keep your programs smaller when they aren't needed. 
# 
# There are a large number of libraries available for Python. Often you need to search online to find the proper library and the proper functions in that library to get the desired job done.
# For the purpose of this class, I shortly introduce a set of widely used libraries and their functions that help us with financial modeling (such as `NumPy`, `Pandas`, `Matplotlib`, `SciPy`, and `Statsmodels`).
# 
# To get the documentation for a library,  go to docs.python.org/3/ and search for the name of  that library (say `NumPy`). Go to that library and review the functions there. You can alternatively, go to Help>Python Documentation in Spyder and search `NumPy` in the index.  You see the same thing.
# 
# 
# A typical way of loading a library is by using the `import LIBRARY_NAME`: e.g. 

# In[69]:


import numpy # which will load the library named NumPy. or
import numpy as np # you can assign a short name for the library too.


# Then you can call the functions inside the library (here the `NumPy` library) by `LIBRARY_NAME.FUNCTION_NAME(INPUT)`. This way, Python will not mix two functions with similar names that are in different libraries.
# 
# 
# You can use the `dir()` command to get the list of functions in each library. For example, after importing the library (say `NumPy`), in the IPython console type `dir(NumPy)` to get the list of functions in the Numpy library. `NumPy` has many functions and some of them are stored in a hierarchy. For example

# In[70]:


import numpy as np
dir(np.lib.financial) 
# this will give the list of some of the financial functions of NumPy


# These functions are equivalent to MS-Excel functions for time value of money:
# 
# `pv()`,`fv()`, `rate()`, `nper()`, `pmt()` (and `ipmt()`, `ppmt()`), `irr()`, (and `mirr()`),`npv()` 

# You can get help documentation for a specific function of a library by using the `help()` function.

# In[71]:


help(np.pv)


# ## NumPy Library
# NumPy is a powerful library that allows data processing on large, multi-dimensional arrays and matrices. Moreover, it provides a large collection of high-level mathematical functions to operate on these arrays.

# In[72]:


import numpy as np           # we use np as the acronym for numpy, for efficiency in typing.
y = np.array([1,2,3,4])      # array is a similar data type to LIST
z = np.sum(y)

print(y)
print(z)


# NumPy provides the core data types for numerical analysis – **arrays** and **matrices**, which are both similar to lists, but arrays and matrices, unlike lists, are always rectangular so that all dimensions have the same
# number of elements. They resemble to the Tables/sheets in MS-Excel. Matrices are essentially a subset of arrays and behave in a virtually identical manner. The two important
# differences are:
# 
# * Matrices always have 2 dimensions, whereas Arrays can have 1, 2, 3 or more dimensions (although in this course we mostly use 2-dimensional arrays to be consistent with the MS-Excel examples)
#     * This means that a `1` by `n` vector stored as an array has `1` dimension and `n` elements, while the same vector stored as a matrix has 2-dimensions where the sizes of the dimensions are `1` and `n` (in either order).
# 
# * Matrices follow the rules of linear algebra for multiplication.     
#     * Standard mathematical operators on arrays operate element-by-element, similar to MS-Excel. This is not the case for matrices, where multiplication `(*)` follows the rules of linear algebra (this makes coding more concise).
#     
# 
# The best practice is to use arrays and to use the `@` symbol for matrix (linear algebra) multiplication. 

# In[73]:


import numpy as np
x = [0.0, 1, 2, 3, 4]
y = np.array(x)
print("An example of a 1-row-4-column vector (1x4):",y)


# In[74]:


y = np.array([[0.0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
print("An example of a 2-row-4-column matrix (2x4):")
print(y)


# ### Merging Two arrays (`concatenate`)
# use `concatenate()` function from the `NumPy` library can help you merge two arrays. Use the `axis` option of the function to define the dimension of the merger:

# In[75]:


x = np.array([[1.0,2.0],[3.0,4.0]])
y = np.array([[5.0,6.0],[7.0,8.0]])
z = np.concatenate((x,y),axis = 0)
print(z)


# In[76]:


z = np.concatenate((x,y),axis = 1)
print(z)


# Alternatively, the functions `vstack()` and `hstack()` can be used to vertically or horizontally stack arrays, respectively.
# 
# `z = vstack((x,y))`  Same as `z = concatenate((x,y),axis = 0)`
# 
# `z = hstack((x,y))`  Same as `z = concatenate((x,y),axis = 1)`

# In MS-Excel, you cannot automatically concatnate arrays or matrixes. You can manually copy and paste the cells you want. This could be a very time consuming process, if you are working with several sheets. Also you might make mistakes. 

# ### Accessing elements of Arrays
# Similar to Lists, you can access:

# In[77]:


x1 = np.array([[1.0,2.0],[3.0,4.0]])
x2 = np.array([[5.0,6.0],[7.0,8.0]])
x3 = np.array([[11.0,22.0],[13.0,24.0]])
x4 = np.array([[52.0,61.0],[37.0,98.0]])
x5 = np.array([52.09,61.02,37.03,98.03,52.03,61.20,37.10,98.2])


# In[78]:


z = np.concatenate((x1,x2,x3,x4),axis = 0)
z = np.hstack((z,x5[:,None]))  # x5 is a 1-dimensional vector. 
                               # by using x5[:,None], we ask Python to treat x5 as a 2-dimensional matrix
print(z)


# In[79]:


print(z[4,2]) # the item in row 5 and column 3 


# In[80]:


print(z[2:4, 0:2 ])  # rows 3 to 4 (exclusive) and columns 1 to 2 (exclusive)


# In[81]:


print(z[:2, ])  # rows 0 & 1  and all columns


# In[82]:


print(z[1:,])  # rows 2 to end and all columns


# In[83]:


print(z[:2,])  # rows 2 to end (every other row) and all columns


# You can reshape your matrix as follows:

# In[84]:


print("z is a matrix of", np.shape(z)[0], "by",np.shape(z)[1] )
print(z)

y = np.reshape(z,(4,6))
print("y is a reshaped matrix of z, which is", np.shape(y)[0],       "by",np.shape(y)[1] )
# I used \ sign to break a long line of code into two shorter ones.
print(y)


# ###  Quick look at arithmetic operations
# * Basic operators:
#   * +, -, *, /: These add, subtraction, multiply, divide.
#   * **: This is to exponentiate (to the power).
#   * //: This is for integer divide (drops fractional part).
#   * %: This is to compute remainder on the division for integers (MOD function in MS-Excel).
# * When  `x` and `y` are scalars, the behavior of these operators is obvious. 
# * When `x` and `y` are arrays the operation is element by element. Therefore, `x` and `y` should be the same size.
# 
# #### Matrix Multiplication
# * Matrix Multiplication is accessible with `@`. If `x` is a matrix with `N` rows and `M` columns (`N by M`) and `y` is `M` by `L`, `z = x @ y` produces an array with `z[i,j] = sum x[i,m] y[m,j]`, where `m=1 to M`. 
# 

# In[85]:


x = np.array([[1.0, 2],[ 3, 2], [3, 4]]) 
print("x =")
print(x)
y = np.array([[9.0, 8],[7, 6]])
print("y =")
print(y)
z = x @ y
print("z =")
print(z)


# In[86]:


# z[0,0] = x[0,0]* y[0,0] + x[0,1]* y[1,0]
# z[0,1] = x[0,0]* y[0,1] + x[0,1]* y[1,1]
# etc


# In[87]:


x = np.random.randn(3,4)      # I will talk about random functions in NumPy later.
print("x = ")
print(x)


# #### Sum, Product and Difference of an Array

# Similar to MS-Excel, in NumPy we have `sum()` and `product()` functions that allow us to get the sum/product of all elements of an array. Let's see some examples:

# Let's consider a  3 by 4 array of random variables. I will talk about random functions in NumPy later, but for now, I only want have a set of arbitrary numbers to work with them:

# In[88]:


x = np.random.randn(3,4)      # 
print("x = ")
print(x)


# In[89]:


print(np.sum(x))   # sum all elements of the array (output = 1 element)


# In[90]:


print(np.sum(x, 0)) # sum the elements of each column, (output = 4 elements)


# In[91]:


print(np.sum(x, 1)) # sum the elements of each row (output = 3 elements)


# `nansum()` is identical to `sum()`, except that NaNs are ignored. NaN, or Not a Number, happens if the input data has missing observations, similar to blank cells in MS-Excel, or whenever a function produces a result that cannot be clearly evaluated to produce a number.
# 
#     * Side Note: `inf` represents infinity and `inf` is distinct from `-inf`.

# Numpy also have a function to create the cumulative sum, which is very useful for financial applications.

# In[92]:


print(np.cumsum(x,0)) # cumulative sum, Down the rows (output = 12 elements)


# In[93]:


print(np.cumsum(x,1)) # cumulative sum, across the columns (output = 12 elements)


# `prod()` and `cumprod()` behave similarly to `sum()` and `cumsum()` except that the product and cumulative product are
# returned. 

# `diff()` generates the difference between elements of an array. This is useful when you want to get how much a company has grown from the previous year, for example, or compute the stock returns.

# In[94]:


z = np.diff(x, axis=0)     # 1st difference between elements of an array
                           # first row of z = second row of x - first row of x
                           # second row of z = third row of x - second row of x
print(z)


# In[95]:


print(np.diff(x, 2, axis=0)) # Double difference, columnbycolumn


# #### Other Simple Math Functions for Array
# 
# Similar to MS-Excel:
# 
# * `exp()` returns the element-by-element exponential (e ^ x ) for an array.
# * `log()` returns the element-by-element natural logarithm (ln(x)) for an array.
# * `log10()` returns the element-by-element base-10 logarithm (log10 (x )) for an array.
# * `sqrt()` returns the element-by-element square root of x
# * `abs()` returns the element-by-element absolute value for an array.

# ### Descriptive Statistics
#  Python has `max()`, `min()`, `sum()` functions to generate some basic descriptive statistics. For other descriptive statistics, such as mean, median, st.dev , variance, ... we can use functions in NumPy Library:
#  * `mean()` and `nanmean()`. in MS-Excel, we have the `AVERAGE()` function
#  * `median()`, in MS-Excel, we have the `MEDIAN()` function
#  * `std()` and `nanstd()`. in MS-Excel we have `STDEV.P()` and `STDEV.S()`
#  * `var()` and `nanvar()`. in MS-Excel we have `VAR.P()` and `VAR.S()`
#  
#  These functions, similar to the `sum()` function allow you to choose the Axis or axes along which the statistics  is computed. The default is to compute the flattened array.
#  
#  Side note: the `STATISTICS` Library in Python also provide summary statistics functions. 
#  
# 
# Example:

# In[96]:


# input variables:
nlist     = [2, 4, 13, 3, 7, 8, 5]
rlist     = [3.14, 2.71, -8.43, 5.25, 10.11, -23.78, 44.45]

print("the maximum of nlist is",max(nlist))
print("the minimum of nlist is",min(nlist))
print("sorted nlist is:",sorted(nlist),       ", the min is the first item:",sorted(nlist)[0],      ", and the max is the last item of the list:",  sorted(nlist)[-1])
print("the sum of nlist is",sum(nlist))


# In[97]:


avg_nlist = np.mean(nlist)
print("The average of nlist is ",avg_nlist)

avg_rlist = np.mean(rlist)
print("The average of rlist is ",avg_rlist)


# In[98]:


median_nlist = np.median(nlist)
print("The median of nlist is",median_nlist)
# alternative way to find the median is:
print("sorted nlist is :",sorted(nlist),       "and the median is the middle item:",sorted(nlist)[len(nlist)//2] )


# In[99]:


print("The standard deviation of rlist is",np.std(rlist))
print("The variance of rlist is",np.var(rlist))


# ### Random Variables
# In Python you can generate random variables with different distributions using the functions in `NumPy` (or `RANDOM`) libraries. 
# 
# Most often we use 4 types of random variables:
# 
# * Uniform Distribution (real numbers)
# 
# This is the case if you want to generate a random number in a range (between `a` and `b`) with equal probability. Example:

# In[100]:


np.random.rand()
# This generates a random number between 0 and 1, each time you call it.


# In[101]:


np.random.rand(3,2)
#Create an array of the given shape (here a 3-by-2 matrix) 
# and populate it with random samples from a uniform distribution over [0, 1).


# * Uniform distribution (integer numbers)
# 
# if you want to generate a random INTEGER number in a range (between `a` and `b`) with equal probability. For example, you want to simulate rolling a six-faced dice  for 10 times:

# In[102]:


np.random.randint(1, high=6+1,size=10)
# This generates 10 random integers between 1 and 6, each time you call it.


# * Uniform distribution (from a set of options):
# 
# For example, if you want to simulate flipping a coin (Heads or Tails):

# In[103]:


coin   =["Head","Tail"]
np.random.choice(coin, size=10) # this will replicate 10 coin flipping


# In[104]:


# you can modify the chance (probability) of the Head or Tail events
# below I set the probability of a Head = 70% (therefore we get more Head outcomes)
np.random.choice(coin, size=10, p=[0.70, 0.30])


# * Normal distribution (bell curve)
# 
# Most random variables in the world are normally distributed (following central limit theorem). A normally distributed random variable is defined with its mean (the center of the bell curve) and its standard deviation (the dispersion around the mean of the bell curve).

# In[105]:


np.random.randn() 
# This generates a standard normal random variable 
# with mean 0 and standard deviation 1
# the output ranges from -inf. to +inf. 


# In[106]:


np.random.randn(3,2) 
# This generates a matrix of 3_by_2 normal random variables


# Let's experiment with random generating functions, as an example:
# 
# The following example builds a sentence using various parts of speech. It randomly chooses words from a list by using `np.random.choice()`. We have used a method of the string data type to capitalize the first letter of the sentence.
# 

# In[107]:


verbs   =["goes","cooks","shoots","faints","chews","screams"]
nouns   =["bear","lion","mother","baby","sister","car","bicycle","book"]
adverbs =["handily","sweetly","sourly","gingerly","forcefully","meekly"]
articles=["a","the","that","this"]

def sentence():
    article = np.random.choice(articles)    
    noun = np.random.choice(nouns)
    verb = np.random.choice(verbs)
    adverb = np.random.choice(adverbs)
    
    our_sentence = article + " " + noun + " " + verb + " " + adverb + "."
    our_sentence = our_sentence.capitalize()
    
    print(our_sentence)


# In[108]:


# call the function to print the random sentence:
sentence()


# #### System of Equations
# * `solve()` solves the system of equations, e.g.:
#     * we have 3 equations and 3 unknowns (a, b, c)
#         * y1 = a x11 + b x21 + c x31
#         * y2 = a x21 + b x22 + c x23
#         * y3 = a x31 + b x32 + c x33
#     * define Y as vector of yi and X as the matrix of xij.

# In[109]:


X = np.array([[1.0,2.0,3.0],[3.0,3.0,4.0],[1.0,1.0,4.0]])
Y = np.array([[1.0],[2.0],[3.0]])
print(np.linalg.solve(X,Y))


# #### Slope Line and Linear Regressions:
# * `lstsq()` solves for  the least squares solution (linear regression) coefficient for 
#     * equation Y = a + bX +u 
#     * a is the intercept, b is the slope and u is the noise. 
#  
# * `lstsq()` returns a 4-element output where 
#     * the first element is [a and b] 
#     * the second element is the sum of squared residuals. 
#     * the third is the rank of X 
#     * the fourth contains the singular values of X.

# In[110]:


X = np.random.randn(1000,1)
a = 5
b = 2
u = np.random.randn(1000,1)
Y =  X * b + u  
print(np.linalg.lstsq(X,Y,rcond=None))


# ### Time Value of Money
# * `npv(rate, values)`
# 
# function in the `NumPy` library offers a similar application to `NPV(rate,value1,[value2],...)` function in MS-Excel to calculate the net present value of a series of future cash flows:

# In[111]:


# Example
# suppose you are asked to calculate the NPV of a project with 
#     initial investment = $ 10 Million
#     cash flows in next 5 years are -2,1,3,10,20 million dollars
#     your required rate of return is at least 10%
DiscountRate = 0.10
CashFlow = np.array([-10,-2,1,3,10,20])*1e6

NPV1 = np.npv(DiscountRate,CashFlow)
print('NPV is',NPV1)
print('NPV is ${:,}'.format(round(NPV1,2)))  
# Notice that I am using a formatting command
# this changes the formatting of the output to currency, with 2 decimals.


#  * `pv(rate, nper, pmt, fv=0, when='end')`
#  
# similarly `pv()` calculates the present value of future cash flows. The cash flows could be an annuity payments (pmt) that are paid at certain dates (such as loan payments), or could be a lump sum payment (fv) paid at maturity (such as the principal of a zero coupon bond), or could be both (such as corporate bonds). 
# 
# Similar to the MS-Excel PV function, the argument `when` defines if it is an **Annuity due**, where the payments are at begins of each period (such as rent and insurance payments), or **Ordinary Annuity**, where payments are paid at the end of each period (such as mortgage and loan payments). Choose `when = {'begin', 1}` or `when = {'end', 0}` depending the application. The default value is `end`.
#  The default value of `fv` is `0`.

# In[112]:


# Example
# suppose you are leasing a car. The cash value of the car is $25,000 (after tax and fees). 
# the car dealer offers you the following:
#     monthly payments of $400 for 3 years, with an interest rate of 1.99% APR.
#     After 3 years, you have the option to pay $ 15,000 are own the car.
#     is this a good deal?

PV1 = np.pv(0.0199/12, 3*12, 400, 15000, 1)
print('PV is ${:,}'.format(round(PV1,2)))  
# this changes the formatting of the output to currency, with 2 decimals.


# That is, if you accept the dealer's offer, including the time value of money, you are paying more than `$28,000` for a car which worth only `$25,000`. So this is a bad deal.

# * `fv(rate, nper, pmt, pv, when='end')` calculates the future value of a stream of cash flows.
# 
# * `rate(nper, pmt, pv, fv, when='end', guess=None, tol=None, maxiter=100)`, finds the required rate of return. For this class, you can ignore the following arguments: `guess`, `tol`, and `maxiter`.
# 
# * `nper(rate, pmt, pv, fv=0, when='end')` computes the number of periodic payments of an annuity.
# * `pmt(rate, nper, pv, fv=0, when='end')` computes the payment against loan principal plus interest. Similarly, `ipmt()` computes the  interest portion of a payment and `ppmt()` computes the payment against loan principal.
# * `irr(CashFlows)` calculates the internal rate of return for a stream of future cash flows (the first element is the initial investment with negative sign). `mirr()` is for modified IRR calculation.

# ## Pandas Library
# `Pandas` library is an increasingly important component of the Python scientific stack. It is a high-performance package that provides a comprehensive set of data structures for working with
# data. `pandas` also provides high-performance, robust methods for importing from and exporting to a wide range of formats, such as xlsx and csv files. Data structures in Pandas allow for labeling columns and rows, which is not available in NumPy. Moreover, it allows for relational-database operations (such as join), which are provided in MS-Access.

# In[113]:


import pandas as pd


# 
# ### Data Structures
# Most important data structures in `pandas` are Series and DataFrames. Series are the equivalent
# of 1-dimensional arrays. DataFrames are collections of Series and so are 2-dimensional (like MS-Excel spreadsheets). 
# 
# #### Series
# Series are the primary building block of the data structures in `pandas`, and in many ways a Series behaves
# similarly to `list` or a `NumPy` `array`. 

# In[114]:


# list
m = [0.1, 1.2, 2.3, 3.4, 4.5]
print(m)


# In[115]:


# NumPy array
a = np.array([0.1, 1.2, 2.3, 3.4, 4.5])
print(a)


# In[116]:


# Panda Series
s = pd.Series([0.1, 1.2, 2.3, 3.4, 4.5])
print(s)


# As we see in the printed values in this example, `pandas` has automatically generated an index for the series using the sequence 0, 1, . . . and when printing or accessing the data you can use it (the first column above).

# In[117]:


# for example, print items with index 0 and 3:
print(s[[0,3]]) 


# You can convert a `NumPy` array to a `Panda`s Series:

# In[118]:


# NumPy array to Series
s = pd.Series(a) 
print(s)


# #### DataFrame
# `DataFrames` collect multiple series in the same way that a spreadsheet collects multiple columns of data.
# A `DataFrame` is composed of `Series` and each `Series` has its own data type, and so not all `DataFrames` are representable as homogeneous NumPy arrays.
# A number of methods are available to initialize a DataFrame. The simplest method uses a homogeneous
# NumPy array.

# In[119]:


a = np.array([[7.0,8,9],[3,4,5]])
df = pd.DataFrame(a)
print(df)


# A `DataFrame` contains column labels and row labels (this feature is also available in `Series`). When none are
# provided, the numeric sequence 0, 1, . . . is used. In the above example, we have three columns that are labelled   `0`, `1` and `2`. There are also two rows labelled as `0` and `1`. 
# Labels are useful when working with large DataFrames, where you do not need to remember which columns stores what values. We can assign column and row names by `columns` and `index` commands:

# In[199]:


a = np.array([[70,80],[90,65],[74,95]])
df = pd.DataFrame(a, columns=['Midterm','Final'], index=['John', 'Sarah', 'Rose'])
print(df)

# alternatively: 
#df = pd.DataFrame(a)
#df.columns = ['Midterm','Final']
#df.index = ['John', 'Sarah', 'Rose']


# Then it is easier to access columns or rows of the DataFrame. You can select a column by giving its name in `[]`, for example:

# In[200]:


print(df['Midterm'])


# Alternatively you can use `.column name` to access a column

# In[201]:


print(df.Midterm)


# To access a row, we can use the `.loc[row name]`:

# In[202]:


print(df.loc['Sarah'])


# In[203]:


print(df.loc['Sarah'].Midterm)


# In[204]:


print(df.loc['Sarah','Midterm'])


# If you don't know the index, you can also access via the row or column number via `.iloc[]` feature:

# In[205]:


print(df.iloc[1,0])


# In[206]:


# or alternatively
print(df.iloc[1].Midterm)


# You can define a new column for the DataFrame using `['new column name']`. e.g:

# In[207]:


df['total'] = df['Midterm']*0.40 + df['Final'] * 0.60
print(df)


# Pandas is built based on NumPy arrays. You can access to it by simply using `.values` feature:

# In[ ]:


df.values
3

# If you want to access to the names of the columns:

# In[ ]:


df.columns


# And if you want to access to the names of the rows (i.e. indexes)

# In[211]:


df.index


# ### Importing and Exporting Data via Panda
# All of the data readers in pandas load data into a pandas `DataFrame`, which if need be you can transfer to a `NumPy` array. 
# In practice, the `DataFrame` is much more useful since it includes useful information such as column names read from the data source. 

# #### Import Excel files
# Excel files, both 97/2003 (xls) and 2007/10/13 (xlsx), can be imported using `read_excel()`. Two inputs are
# required to use `read_excel()`, the FILE_NAME and the SHEET_NAME containing the data. In this example, pandas
# makes use of the information in the Excel workbook that the first column contains dates and converts
# these to datetimes. Like the mixed CSV data, the array returned has object data type.

# In[127]:


excel_data = pd.read_excel('FTSE_1984_2012.xls','FTSE_1984_2012')
print(excel_data)


# Other notable keyword arguments while importing include:
# * `header`, an integer indicating which row to use for the column labels. The default is 0 (top) row, and if `skiprows` is used, this value is relative.
# * `skiprows`, typically an integer indicating the number of rows at the top of the sheet to skip before reading the file. The default is 0.
# * `skip_footer`, typically an integer indicating the number of rows at the bottom of the sheet to skip when reading the file. The default is 0.
# * `index_col`, an integer or column name indicating the column to use as the index. If not provided, a basic numeric index is generated.
# * `usecols=[0,1,2,3]`, only import columns 1 to 4.
# 

# #### Import CSV and other formatted text files
# Comma-separated value (CSV) files can be read using `read_csv()`. CSV files are text-base files and do not have Excel meta data (formatting embeded in cells; for example, they cannot have several sheets or cell formatting). Because of this, for many software programs they are easier to connect to, compared to Excel.

# In[128]:


csv_data = pd.read_csv('FTSE_1984_2012.csv')


# #### Export using Pandas
# Writing data from a Series or DataFrame is much simpler since the starting point (the Series or the DataFrame)
# is well understood by pandas. While the file writing methods all have a number of options, most can safely
# be ignored.

# In[129]:


# state_gdp.to_excel('state_gdp_from_dataframe.xls')
# state_gdp.to_excel('state_gdp_from_dataframe_sheetname.xls', sheet_name='State GDP')
# state_gdp.to_excel('state_gdp_from_dataframe.xlsx')
# state_gdp.to_csv('state_gdp_from_dataframe.csv')


# ### Manipulating Data in Pandas
# #### Summary 

# `head()` returns the first 5 rows of a DataFrame, to give you a sense of the data in a glance:

# In[223]:


state_gdp = pd.read_excel('US_state_GDP.xls','Sheet1')
state_gdp.head()


# In[224]:


# if you are only interested in a few columns of your DataFream, just select them
# for example, below I choose two columns and see their first 5 rows
state_gdp_2012 = state_gdp[['state','gdp_2012']]
state_gdp_2012.head()


# Similarly, you can use the `tail()` function to get the last 5 observations of a DataFrame.

# You can access to (and modify) the name of the columns by using `.columns` feature:

# In[225]:


state_gdp.columns


# #### Statistical Functions
# 
# Simple statistical functions such as `sum`, `mean`, `std`, `var`, `prod`, `median`, `quantile`, `abs`, `cumsum` (cumulative sum), and `cumprod` (cumulative product) are available for Series and DataFrame. DataFrame also supports `cov` and `corr` – the keyword argument axis determines the direction of the operation (0 for down columns, 1 for across rows). 
# 
# `describe()` returns a simple set of summary statistics (number of non-missing observations, average, standard deviation, ...). The values returned is a series where the index
# contains the names of the statistics computed.

# In[226]:


df = state_gdp[['state','gdp_2009', 'gdp_2010','gdp_2012']]
df.describe()


# Notice that we can get each of the above separately too:

# In[227]:


df.mean()


# In[228]:


df.std()


# In[229]:


df.min()


# In[230]:


df.quantile([0.25,0.50,0.75])


# In[231]:


df.max()


# `count` returns the number of non-null values – that is, those which are not NaN or another null value such as
# None or NaT (not a time, for datetimes).
# `value_counts` performs histogramming of a Series or DataFrame.

# In[232]:


state_gdp.region.value_counts()


# #### Aggregation 
# The simplest application of `groupby` is to aggregate statistics such as group means or extrema. All aggregation
# functions will return a single value per column for each group. Many common aggregation functions
# have optimized versions provided by `pandas`. For example, `mean`, `sum`, `min`, `std`, and `count` can all be directly
# used on a `DataFrame GroupBy` object.

# In[233]:


# Generate the average GDP growth rate for each region in 2009 and 2010:

# First, select the columns needed
cols = ['gdp_growth_2009','gdp_growth_2010','region','state']
df_gdp_subset = state_gdp[cols]
df_gdp_subset.head()


# In[239]:


# Second, use the groupby function to group the data
grouped_data = df_gdp_subset.groupby('region')
# Third, use the mean function to give the average values:
grouped_data.mean()


# In[240]:


# We can also groupby two columns, say region and state
df_gdp_subset.groupby(['region','state']).mean()


# In[ ]:


# If we want, we can limit ourselves to a column
df_gdp_subset.groupby(['region'])['gdp_growth_2009'].mean()


# If the function we are working with is not included in Pandas default functions (e.g. `mean`, `sum`, `min`, `std`, and `count`), we can use the `.agg(MyFunction)` feature, where `MyFunction` is our function of choice.
# Below, I defined a function (named `sumsq()`) which sums the square of each item.

# In[245]:


def sumsq(x):
    return sum(x**2)
df_gdp_subset.groupby(['region'])['gdp_growth_2009'].agg(sumsq)


# #### Copy a DataFrame (or part of it)
# to ensure that a new DataFrame contains its own copy of the original data and is not sharing with it, use `.copy()`:

# In[143]:


state_gdp_2012 = state_gdp[['state','gdp_2012']].copy()
state_gdp_2012.head()


# #### Delete columns of a DataFrame
# `.drop(list of columns,axis=1)` will return a DataFrame with the Series dropped without modifying the original DataFrame.

# In[144]:


state_gdp_dropped = state_gdp_2012.drop(['state'],axis=1)
state_gdp_dropped.head()


# `drop(labels)` drops rows based on the row labels in a label or list labels. For example, drop row 4 (California):

# In[145]:


state_gdp_dropped = state_gdp_2012.drop(4)
state_gdp_dropped.head()


# Finally, `drop_duplicates()` removes rows which are duplicates or other rows, and is used with the keyword argument `drop_duplicates(cols=col_list)` to only consider a subset of all columns when checking for duplicates.

# In[146]:


df = pd.DataFrame(np.array([[70,80, 5],[90,65,1],[74,95,3],[70,80,4]]) )
print('df = ')
print(df)

print('unique values of the first column of df = ',pd.unique(df[0]))

df_drop_duplicates = df.drop_duplicates([0,1])
print('drop rows with duplicate values in the first and second columns: ')
print(df_drop_duplicates)


# #### Melting a DataFrame
# For some applications, it might be needed to work with vectorize data. For example, for the GDP example above, you might want to transfer the data to

# | Stretch/Untouched | ProbDistribution | Accuracy |
# | --- | --- | --- |
# | Stretched | Gaussian | .843 |

# | index| state | region | Variable |Year | Amount |
# | ---  | ---   | ---    | ---      | --- | --- |	     	      	
# |0 |	Alaska |	FW |	gdp |2009 |	44215.0
# |1 |	Alabama |	SE |	gdp |2009 |	149843.0
# |2 |	Arkansas |	SE |	gdp |2009 |	89776.0
# |--- | --- | --- | --- | --- | --- |
# |403 | 	Vermont 	| NE |	gdp_growth | 2012 |	1.2
# |404 |	Washington |	FW |	gdp_growth |2012 |	3.6
# |405 |	Wisconsin |	GL 	|gdp_growth | 2012 |	1.5

# For this, first we need to select the identifiers (e.g. `state`,`region`). Then we select the columns that we want to vectorize (here, `gdp_2009`, `gdp_2010`,..., `gdp_growth_2011`,`gdp_growth_2012`). Then we assign a name to the variables and the variables values. See below:

# In[147]:


GDP_vectorized = state_gdp.melt([ 'state','region'],[ 'gdp_2009', 'gdp_2010', 'gdp_2011', 'gdp_2012',
       'gdp_growth_2009', 'gdp_growth_2010', 'gdp_growth_2011','gdp_growth_2012'],'Variable_Year','Amount')
GDP_vectorized.head()


# We are almost done. We just need to extract the dates from the Variable names above and store it in a Year column. The last four digits of the Variable is the year. So take it out.

# In[148]:


GDP_vectorized['Variable'] = GDP_vectorized['Variable_Year'].apply(lambda s: s[:-5])
GDP_vectorized['Year']     = GDP_vectorized['Variable_Year'].apply(lambda s: int(s[-4:]))
GDP_vectorized.head()


# Then you can easily take querries from the dataset. For example:

# In[149]:


GDP_vectorized.query('state == "Alaska"')


# In[150]:


GDP_vectorized.query('Year == "2010" and Variable == "gdp_growth" and region == "SE"')


# #### Transpose a DataFrame
# `.T` transposes a DataFrame (change the columns and rows):

# In[151]:


a = np.array([[70,80],[90,65],[74,95]])
df = pd.DataFrame(a, columns=['Midterm','Final'], index=['John', 'Sarah', 'Rose'])
print('The original data:')
print(df)
print('The transpose of the original data:')
print(df.T)


# #### Sort
# `sort_values` sorts the contents of the DataFrame along either axis using the contents of a single column or row. Passing a list of columns names or index values implements lexicographic search. `sort_index` will sort a DataFrame by the values in the index.
# Both support the keyword argument `ascending` to determine the direction of the sort (`ascending` by
# default). `ascending` can be used with a list to allow sorting in different directions for different sort variables.

# In[152]:


a = np.array([[70,80],[90,65],[74,95],[74,70]])
df = pd.DataFrame(a, columns=['Midterm','Final'], index=['John', 'Sarah', 'Rose','Adam'])
df.sort_values(by='Midterm')


# In[153]:


df.sort_values(by=['Midterm','Final'])


# In[154]:


df.sort_values(by=['Midterm','Final'], ascending=[0,1])


# #### Merge and Join DataFrames
# `merge` and `join` provide SQL-like operations for merging the DataFrames using row labels or the contents
# of columns. In MS-Excel, you can use `LOOKUP` function for merging. 
# 
# The primary difference between the two is that `merge` by default uses column contents while
# `join` defaults to using index labels. Both commands take a large number of optional inputs. The important
# keyword arguments are:
# 
# * `how`, which must be one of 'left', 'right', 'outer', 'inner' describes which set of indices to use when performing the join. 
# 
#     * 'left' uses the indices of the DataFrame that is used to call the method and 'right' uses the DataFrame input into merge or join. 
# 
#     * 'outer' uses a union of all indices from both DataFrames and 'inner' uses an intersection from the two DataFrames.
# 
# * `on` is a single column name or list of column names to use in the merge. `on` assumes the names are common. If no value is given for `on` or `left_on/right_on`, then the common column names are used.
#     * `left_on` and `right_on` allow for a merge using columns with different names. When `left_on` and
# `right_on` contain the same column names, the behavior is the same as `on`.
# 
# * `left_index` and `right_index` indicate that the index labels are the join key for the left and right DataFrames.

# In[198]:


df_left = pd.DataFrame([['a','b'],['c','d'],['e','f']],columns=['one','two'])
print('df_left:')
print(df_left)

df_right = pd.DataFrame([['a','b'],['c','d'],['g','h']],columns=['one','three'])
print('df_right:')
print(df_right)


# In[156]:


# merge the second column of DataFrame df_right with df_left, 
# where the values of items in column ONE of the two DataFrame are the same.
# drop rows that do not have shared values in column ONE
df_left.merge(df_right,on='one') 
# This is the same as how='inner'


# In[157]:


# merge the second column of DataFrame df_right with df_left, 
# where the values of items in column one of the two DataFrame are the same.
# keep all rows of DataFrame df_left and put NaN if cannot find the match
df_left.merge(df_right,on='one', how='left')


# In[158]:


# merge the second column of DataFrame df_right with df_left, 
# where the values of items in column one of the two DataFrame are the same.
# keep all rows of DataFrame df_right and put NaN if cannot find the match
df_left.merge(df_right,on='one', how='right')


# In[ ]:


# merge the second column of DataFrame df_right with df_left, 
# where the values of items in column one of the two DataFrame are the same.
# keep all rows of both DataFrames and put NaN if cannot find the match
df_left.merge(df_right,on='one', how='outer')


# Another example: 
# Below, I list US presidents, their inaguration date, and birthday. In a different DataFrame, I list their fathers name. Then I merge them when the (president) name in the first DataFrame equals the son (name) in the second DataFrame:

# In[218]:


presidents = pd.DataFrame([{'name': 'Barack Obama','inauguration': 2009,'birthyear': 1961},
                          {'name': 'George W. Bush','inauguration': 2001,'birthyear': 1946},
                          {'name': 'Bill Clinton','birthyear': 1946,'inauguration': 1993},
                          {'name': 'George H. W. Bush','inauguration': 1989,'birthyear': 1924}])
presidents


# In[219]:


presidents_fathers = pd.DataFrame([{'son': 'Barack Obama','father': 'Barack Obama, Sr.'},
                                   {'son': 'George W. Bush','father': 'George H. W. Bush'},
                                   {'son': 'George H. W. Bush','father': 'Prescott Bush'}])
presidents_fathers


# In[220]:


df = pd.merge(presidents,presidents_fathers,left_on='name',right_on='son')
df


# In[ ]:


# Son name and the President names are the same, so drop it.
df = pd.merge(presidents,presidents_fathers,left_on='name',right_on='son').drop('son',axis=1)
df


# In[222]:


# Notice that I did not include Bill Clinton in the presidents_father DataFrame. 
# it is missing from DF. 
# to include it, we can use HOW:
df = pd.merge(presidents,presidents_fathers,left_on='name',right_on='son', how = 'left').drop('son',axis=1)
df


# ### Time-series Data
# A TimeSeries is basically a series where the index contains datetimes index values (more formally
# the class `TimeSeries` inherits from `Series`), and `Series` constructor will automatically promote a Series
# with datetime index values to a TimeSeries. 
# 
# TimeSeries have some useful indexing tricks. 
# 
# For instance, in the example below, all of the data for a particular year (here 2009) can be retrieved using gdp['yyyy'] syntax where yyyy is a year.

# In[160]:


# Print GDP data of year 2009

# 1. read 'GDPC1.xls'
GDP_data = pd.read_excel('GDPC1.xls','GDPC1',skiprows=19)

# 2. print the first 5 rows of 'GDPC1.xls'
print('First 5 rows:')
print(GDP_data.head())
print('')

# 3. describe the DATE column of 'GDPC1.xls'
print('Summary Statistics of the DATE column:')
print(GDP_data.DATE.describe())
print('')

# 4. print GDP data from year 2009
print('GDP in Year 2009:')
gdp = GDP_data.VALUE
gdp.index = GDP_data.DATE
print(gdp['2009'])


# Similarly, you can access to a month, a date, or a period of time of a TimeSeries:

# In[161]:


#  GDP data of second quarter of 2009
gdp['2009-04']


# In[162]:


# GDP data of year 2007 to 2009 (inclusive)
gdp['2007':'2009']


# You can also play with Time and Dates in Pandas with its `.dt` feature. For example, to get the year of the dates we can do:

# In[163]:


GDP_data['Year'] = GDP_data.DATE.dt.year
GDP_data['Quarter'] = GDP_data.DATE.dt.quarter
GDP_data['Month'] = GDP_data.DATE.dt.month
GDP_data['Week'] = GDP_data.DATE.dt.week
GDP_data['Day of the Week'] = GDP_data.DATE.dt.weekday_name
GDP_data['Day'] = GDP_data.DATE.dt.day

print(GDP_data.head())


# If the DATE column was stored as a string (`str`), you can change it to Pandas Time-Date series, using `pd.to_datetime(GDP_data.DATE)`. Then you can work with the above `.dt` functions.

# #### Returns
# A more useful application of TimeSeries data is for financial time series, where we are interested in the growth rates (or rate of return) in a period. For example, in the dataset above, we can calculate the GDP growth rate.
# Growth rates are computed using `pct_change()`. 

# In[164]:


gdp.pct_change().tail() # Here tail gives the last 5 observations


# The keyword argument periods constructs overlapping growth rates which are useful when using seasonal data. For example, in our dataset, which is at the quarterly frequncy, you can get the annual growth rate, with respect to the 4 quarters ago GDP.

# In[165]:


gdp.pct_change(periods=4).tail() # Quarterly data, annual difference


# In[166]:


# Alternatively, you can aggregate the quarterly GDP data to annual data
GDP_annual = gdp.resample("1y").sum()
GDP_annual = pd.DataFrame(GDP_annual)
GDP_annual.pct_change().tail()


# In[167]:


gdp.pct_change(periods=4).describe()


# In[168]:


GDP_annual = gdp.resample("1y").sum()
GDP_growh_annual = gdp.pct_change


# The `pct_change()` function is very useful for analyzing the stock returns. Most financial databases provide a time series for the price of a company and you can use this function to get the holding period returns.
# 
# The TimeSeries is also a useful datastructure for plotting financial data. In the next section, I will explain the basics of plotting with Python. 

# ### Pandas_datareader
# This library allows you to download data from several websites such as Yahoo Finance, Google Finance, Morningstar, St.Louis FED (FRED) and Kenneth French’s data library. Check the documentation of the library for more details here: https://pandas-datareader.readthedocs.io/en/latest/remote_data.html
# 
# 
# You need to first install this library as it is not included in the main package during the installation. Launch Aanadoconda Prompt (from the Start menu of Windows or the Mac equivalent) then type/run: `pip install pandas_datareader`. It will download and install it on your machine.

# #### Stock Prices
# We can use Yahoo Finance, Google Finance, and Morningstar wesbites to get the stock prices of companies using their Ticker Symbol.The example below shows how to download the closing price for three companies:

# In[5]:


import pandas_datareader.data as pdr

# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
tickers = ['AAPL', 'MSFT', '^GSPC']

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2010-01-01'
end_date = '2016-12-31'

# User pandas_reader.data.DataReader to load the 
# stock prices from Yahoo Finance. 

panel_data = pdr.DataReader(tickers, 'yahoo', start_date, end_date)
# panel_data = pdr.DataReader(tickers, 'morningstar', start_date, end_date)

# Yahoo Finance gives 'High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close'.

Close_Price = panel_data['Close']
Close_Price.head()


# In[7]:


# Get monthly data from daily data
Close_Price_monthly = Close_Price.resample("1m").ffill()
Close_Price_monthly.head()


# #### Economics Data
# We can use the website of Federal Reserve Bank of St.Louis (FRED) or World Bank. For example, below we can download US GDP data:

# In[ ]:


import pandas_datareader.data as pdr
GDP_data = pdr.DataReader('GDP', 'fred', '2010-01-01', '2016-12-31')
GDP_data.head()


# #### Portfolio Data from Fama French
# We can access the datasets on the Fama/French Data Library (http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html) via Pandas_datareader. The `get_available_datasets` function returns a list of all available datasets.

# In[9]:


import pandas_datareader.data as pdr
from pandas_datareader.famafrench import get_available_datasets


# In[16]:


# Fama French Data library has about 260 datasets. See the first 5 of them below
get_available_datasets()[:4]


# In[22]:


Industry_Portfolios = pdr.DataReader('5_Industry_Portfolios', 'famafrench')


# This file was created by CMPT_IND_RETS using the 201712 CRSP database. It contains value- and equal-weighted returns for 5 industry portfolios. The portfolios are constructed at the end of June. The annual returns are from January to December. Missing data are indicated by -99.99 or -999. Copyright 2017 Kenneth R. French
# 
#   0 : Average Value Weighted Returns -- Monthly (96 rows x 5 cols)
#   
#   1 : Average Equal Weighted Returns -- Monthly (96 rows x 5 cols)
#   
#   2 : Average Value Weighted Returns -- Annual (8 rows x 5 cols)
#   
#   3 : Average Equal Weighted Returns -- Annual (8 rows x 5 cols)
#   
#   4 : Number of Firms in Portfolios (96 rows x 5 cols)
#   
#   5 : Average Firm Size (96 rows x 5 cols)
#   
#   6 : Sum of BE / Sum of ME (8 rows x 5 cols)
#   
#   7 : Value-Weighted Average of BE/ME (8 rows x 5 cols)

# In[27]:


Industry_Portfolios[0].head()


# # Graphics
# `Matplotlib` is a complete plotting library capable of high-quality graphics. Here I cover the basics of producing
# plots. Further information is available on the `matplotlib` website (`https://matplotlib.org/`).

# In[169]:


import matplotlib.pyplot as plt
import seaborn as sns   
# seaborn is a Python package which provides a number of advanced data visualized plots. 
# It also provides a general improvement in the default appearance of matplotlib-produced plots.


# ## Line Plot
# The most basic, and often most useful 2D graphic is a line plot. Basic line plots are produced using `plot(INPUT_VARIABLE)`
# using a single input containing a 1-dimensional array.

# In[170]:


y = np.random.randn(100)
plt.plot(y)


# You can modify the line color, line style or the marker on the graph by adding the Format strings, which may contain any of the following elements:
# 
# * Color 
#     * `b` for Blue  
#     * `g` for Green
#     * `r` for Red
#     * `c` for Cyan 
#     * `m` for Magenta 
#     * `y` for Yellow
#     * `k` for Black
#     * `w` for White 
# * Line Style
#     * `-` for Solid 
#     * `--` for Dashed
#     * `-.` for Dash-dot
#     * `:` for Dotted
# * Marker 
#     * `.` for Point
#     * `o` for Circle
#     * `s` for Square
#     * `d` for Thin Diamond
#     * `x` for Cross
#     * `+` for Plus
#     * `*` for Star
#     
# For example:

# In[171]:


plt.plot(y,'g*-.')


# If you want to plot the variable `y` in the vertical axis with respect to the variable `x` in the horizontal axis you can use `plt.plot(x,y)`

# In[172]:


x = np.cumsum(np.random.rand(100))  # define variable `x`.
plt.plot(x,y)


# You can add multiple lines in a graph like below:

# In[173]:


x = np.cumsum(np.random.randn(100,3), axis = 0)
plt.plot(x[:,0],'b',
label = 'Series 1')
plt.plot(x[:,1],'g.',
label = 'Series 2')
plt.plot(x[:,2],'r:',label = 'Series 3')
plt.legend(loc = 0, frameon = False)
plt.title('Figure1: Basic Legend')


# In[174]:


# Back to our GDP example:
# Plot End of year (annual) GDP and annual GDP growth rate in one plot

# 1. To get the annual GDP, we need to take sum of quarterly GDP data.
GDP_annual = gdp.resample("1y").sum()
# 2. then take the growth rates
GDP_annual_growth = GDP_annual.pct_change()

# 3. In order to have two y-axis,
# 3.1. share the x axis between the two plots
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
# 3.2. plot the series
ax1.plot(GDP_annual_growth,'g*-.')
ax2.plot(GDP_annual,'b')

# 3.3. Add y-labes
ax1.set_ylabel('GDP Growth Rate', color='g')
ax2.set_ylabel('Annual GDP', color='b')

# 3.4. Add a title and the x-label
plt.title('GDP and GDP Growth Rate')
ax1.set_xlabel('Year')


# ## Scatter Plots
# Similarly, we can draw scatter plots with `Matplotlib` library. 

# In[175]:


# Example:
# 1. generate 2 normal random variables, each series with 100 observations
z = np.random.randn(100,2) 

# 2. define two variables x and y based on the randomly generated variables
# e.g. set the variable y a unit variance with correlation of 50% with the variable x.
# this makes sure that the scatter plot would have a 1-to-2 slope.
x = z[:,0]
y = 0.5*z[:,0] + np.sqrt(0.5)*z[:,1] 

plt.scatter(x,y)


# ## Bar Charts
# `bar` produces bar charts using two 1-dimensional arrays. The first specifies the left edge of the bars and
# the second the bar heights. For example:

# In[176]:


y = np.random.rand(5)
x = np.arange(5)
plt.bar(x,y)


# ## Pie Charts
# `pie` produces pie charts using a 1-dimensional array of data (the data can have any values, and does not
# need to sum to 1). e.g.:

# In[177]:


y = np.random.rand(5)
y = y/sum(y)
y[y<.05] = .05
plt.pie(y)


# Pie charts can be modified using a large number of keyword arguments, including labels and custom
# colors. Exploded views of a pie chart can be produced by providing a vector of distances to the keyword argument explode.
# Note that `autopct = '%2.0f'` is using an old style format string to format the numeric labels. 

# In[178]:


explode = np.array([.2,0,0,0,0])
labels = ['Apple', 'Google', 'Amazon', 'IBM', 'Facebook']
plt.pie(y, explode = explode, labels = labels, autopct = '%2.0f', shadow = True)


# ## Histograms
# Histograms can be produced using `hist`. Histograms show the frequency of repeated values in your data. See the example below, which sets the number of bins used in producing the histogram using the keyword argument bins.

# In[179]:


x = np.random.randn(1000)
plt.hist(x, bins = 30)


# Histograms can be further modified using keyword arguments. In the next example, `cumulative=True` produces
# the cumulative histogram. 

# In[180]:


plt.hist(x, bins = 30, cumulative=True, color='r')


# # Solver and Optimizer 
# `SciPy` library contains a number of routines to the find extremum (minimum or maximum) of a user-supplied objective function located in `scipy.optimize`. `SciPy` has more useful functions but for the sake of this class we only focus on the optimization functions.

# In[181]:


import scipy.optimize as opt


# The steps are similar to the Solver add-on in MS-Excel. First we need to define an (objective) function that we want to minimize. For example, consider finding the minimum of $x^2$. A function which
# allows the optimizer to work correctly has the form

# In[182]:


def optim_target1(x):
    return x**2


# Once an optimization target has been specified, the next step is to use one of the optimizers find the minimum. That is you need to call the Python optimizer functions to find the minimum of your objective function. Optimizers are categorized into two main types: unconstrained and constrained optimizers. If the parameters in mind are limited in a range, we use constrained optimizers. On the other hand, if the parameters of the objective function can take any value then use unconstrained optimizers.

# ## Unconstrained Optimizers
# The basic structure of all of the unconstrained optimizers is `optimizer(f, x0)` where `optimizer` is one of `fmin_bfgs, fmin_cg, fmin_ncg or fmin_powell` functions in SciPy library. `f` is your objective function and `x0` is a set of initial values used to start the algorithm. For this course, we mostly use `fmin_bfgs`, which is the simplest optimizer.
# Back to our example above:

# In[183]:


opt.fmin_bfgs(optim_target1, 1)


# The optimizer `fmin_bfgs` finds that at `x = -7.45036449e-09` our objective function ($x^2$) reached to its minimum value, which is `Current function value: 0.000000`. 
# Notice that the correct theoretical answer is `x=0`, but numerically Python finds `x = -0.000000000745036449`, is accurate to 9 decimal places.

# We can modify our objective function to solve it. Say we want to know at what value of `x` the objective function becomes 4. 
# The idea is to define a new objective function and find the minimum distance of the initial objective function (i.e. $x^2$) and 4

# In[184]:


def optim_target2(x):
    return abs(x**2 - 4)
opt.fmin_bfgs(optim_target2, 1) 


# The optimizer finds that at `x = 1.99999999` our objective function ($x^2-4 $) equals to its minimum value (i.e.`0.000000`). 
# Notice that the correct theoretical answer is `x=2`, and the numerical solution is accurate to 8 decimal places.

# **More Complex Cases**:
# Imagine the case where the objective function has multiple parameters (a parameter vector). In that case, define the  objective function in the following form

# In[185]:


def optim_target3(params):
    x, y = params
    return x**2 - 3*x + 3 + y*x -3*y + y**2


# Another case, would be to have an objective function that requires additional inputs, which are not parameters of interest. In this case, define the objective function in the following form:

# In[186]:


def optim_target4(params, hyperparams):
    x, y = params
    c1, c2, c3 = hyperparams
    return x**2 + c1*x + c2 + y*x + c3*y + y**2


# This form is especially useful when optimization targets require both parameters and data. Additional inputs are can be passed to the optimization target using the keyword argument `args` and a
# tuple containing the input arguments in the correct order. In the above example, we have a single additional input, therefore the comma is necessary in `(hyperp,)` to let Python know that this is a `tuple`. E.g:

# In[187]:


# the syntax would be to include arg = (extra inputs,)
param0 = [1,2]
hyperparams = [5,0.1,3]
opt.fmin_bfgs(optim_target4, param0, args=(hyperparams,) )


# ## Constrained Optimization
# Constrained optimization is frequently encountered in financial problems where parameters are only meaningful in some particular range – for example, the weights in an investment portfolio must be positive (no short selling) or the weights cannot be larger than 10%.
# 
# More formally the constrained optimization problems can be formulated:
# 
# $$
# min_\theta \;\; f(\theta) \;\; \text{subject to} \\
# g(\theta) = 0 \;\; \text{(equality)} \\
# h(\theta) \ge 0 \;\;\; \text{(inequality)} \\
# \theta_L \le \theta \le \theta_H \;\; \text{(bounds)}\\
# $$
# 
# where the `f` is the objective function, `g` and `h` are the set of equations for the equality and inequality constraints on the parameters. 

# The function `fmin_slsqp` is the most general constrained optimizer and allows for equality, inequality and bounds constraints.
# Constraints (here the functions `g` and `h`) are provided either as a list of callable functions or as a single function which returns an array. The latter is simpler if there are multiple constraints, especially if the constraints can be easily calculated using linear
# algebra. 

# As an example, let's consider a simple consumption optimization. I want to buy ice cream and chocolate. Let's assume their joint utility (pleasure) is calculated with a  CRS Cobb-Douglas utility function:  $U(x_{i}, x_{c}) = x_{i}^\alpha \; x_{c} ^ {1-\alpha}$, where $x_i, x_c$ show the quantity of the ice cream and chocolate that I purchase. $\alpha$ is my personal preference for each item (e.g. my $\alpha = 0.33$ because I favor chocolate more than ice cream, by order of 2). I am subject to a budget constraint (say I have only `$15` to buy these): $p_{i} x_{i} + p_{c} x_{c} \le 15$, where $p$ shows the price of each item. Let's assume each scope of ice cream costs `$2`  and each chocolate bar costs `$10` (i.e. $p_i = 2 \;\; \text{and}\;\; p_c = 10 $). 
# Obviously the other constraint is that the quantity of each item I purchases cannot be negative. That is: $x_{i}\ge 0$ and $x_{c} \ge 0$). 

# We first need to specify the objective function

# In[188]:


def utility(x, p, alpha):
    return -1.0 * (x[0]**alpha)*(x[1]**(1-alpha))
# Notice that the optimizer finds the minimum, not maximum.
# So we multiply the output by -1 


# Then we need to define the 3 constraints (budget and non-negative purchases)

# In[189]:


def utility_constraints(x, p, alpha):
    return np.array([x[0], x[1], 15- p[0]*x[0]- p[1]*x[1]])


# Let's find out how many scoops of ice cream and how many bars of chocolate I should buy:

# In[190]:


p = np.array([2.0,10.])
alpha = 1.0/3
x0 = np.array([.4,.4])
opt.fmin_slsqp(utility, x0, f_ieqcons=utility_constraints, args=(p, alpha))


# That means my optimal decision is to buy 2.5 scoops of ice cream and 1 bar of chocolate.

# # Python Coding Conventions
# There are a number of common practices which can be adopted to produce Python code which looks
# more like code found in other modules:
# 
# 1. Use self-explanatory names for the variables and DataFrame. Something that you would quickly understand when you look at your codes
# 
# 1. try to add sufficient comments and annotations to your codes so that you can understand your work later.
# 
# 1. Use 4 spaces to indent blocks – avoid using tab, except when an editor automatically converts tabs to 4 spaces
# 
# 2. Avoid more than 4 levels of nesting, if possible
# 
# 3. Limit lines to 79 characters. The `\` symbol can be used to break long lines
# 
# 4. Use two blank lines to separate functions, and one to separate logical sections in a function.
# 
# 5. Use ASCII mode in text editors, not UTF-8
# 
# 6. One module per import line
# 
# 7. Avoid `from` *module* `import * ` (for any module). Use either `from` *module* `import` *func1, func2* or `import` *module* `as` *shortname*.
# 
# 8. Follow the NumPy guidelines for documenting functions
# More suggestions can be found in *PEP8 Style Guide for Python Code* (`https://www.python.org/dev/peps/pep-0008/`)
# 
# # References and Python Resources
# Python is an increasingly popular programming  language. You can find numerous useful tutorials on it on the web. For this document, I personally consulted the following materials frequently:
# 
# * On www.Coursera.org, the "Python Programming: A Concise Introduction" online course by Bill Boyd
# 
# * On www.kevinsheppard.com, the "Introduction to Python for Econometrics, Statistics and Data Analysis" course by Kevin Sheppard
# 
# * On www.Lynda.com, the "Python: Data Analysis" and "Python Statistics Essential Training" courses, by Michele Valisneri, available(UOIT students have free access to all courses on Lynda)
# 
# * Python forum on www.stackoverflow.com
# 
# * and, many tutorials on www.YouTube.com
# 
# ## Best Python Libraries/Packages for Finance and Financial Data Scientists
# 
# An article from Majid AliAkbar (https://www.linkedin.com/pulse/best-python-librariespackages-finance-financial-data-majid-aliakbar/), Published on March 28, 2017.
# 
# Finance professionals involved in data analytics and data science make use of R, Python and other programming languages to perform analysis on a variety of data sets. Python has been gathering a lot of interest and is becoming a language of choice for data analysis. Python also has a very active community which doesn’t shy from contributing to the growth of python libraries. If you search on Github, a popular code hosting platform, you will see that there is a python package to do almost anything you want.This article provides a list of the best python packages and libraries used by finance professionals, quants, and financial data scientists.
# 
# * Numerical, Statistical & Data Structures
# 
#     * `numpy` – NumPy is the fundamental package for scientific computing with Python. It is a first-rate library for numerical programming and is widely used in academia, finance, and industry. NumPy specializes in basic array operations.
#     * `scipy` – SciPy supplements the popular Numeric module, Numpy. It is a Python-based ecosystem of open-source software for mathematics, science, and engineering. It is also used intensively for scientific and financial computation based on Python
#     * `pandas` – The pandas library provides high-performance, easy-to-use data structures and data analysis tools for the Python programming language. Pandas focus is on the fundamental data types and their methods, leaving other packages to add more sophisticated statistical functionality
#     * `quantdsl` – Quand DSL is domain specific language for quantitative analytics in finance and trading. Quant DSL is a functional programming language for modeling derivative instruments.
#     * `statistics` – This is a built-in Python library for all basic statistical calculations
# 
# * Financial Instruments
# 
#     * `pyfin` – Pyfin is a python library for performing basic options pricing in python
#     * `vollib` – vollib is a python library for calculating option prices, implied volatility and greeks using Black, Black-Scholes, and Black-Scholes-Merton. vollib implements both analytical and numerical greeks for each of the three pricing formulae.
#     * `QuantPy` – A framework for quantitative finance In python. Some current capabilities: Portfolio class that can import daily returns from Yahoo, Calculation of optimal weights for Sharpe ratio and efficient frontier, and event profiler
#     * `ffn` – A financial function library for Python. ffn is a library that contains many useful functions for those who work in quantitative finance. It stands on the shoulders of giants (Pandas, Numpy, Scipy, etc.) and provides a vast array of utilities, from performance measurement and evaluation to graphing and common data transformations.
#     * `pynance` – PyNance is open-source software for retrieving, analyzing and visualizing data from stock and derivatives markets. It includes tools for generating features and labels for machine learning algorithms.
#     * `tia` – TIA is a toolkit that provides Bloomberg data access, easier pdf generation, backtesting functionality, technical analysis functionality, return analysis and few windows utils.
# 
# * Trading & Backtesting
# 
#     * `TA-Lib` – TA-Lib is widely used by trading software developers requiring to perform technical analysis of financial market data. It has an open-source API for python.
#     * `trade` – trade is a Python framework for the development of financial applications. A trade app works like a service. The user informs the items he has in stock and a series of subsequent occurrences (purchases, sales, whatsoever) with those or other items. trade then calculates the effects of those occurrences and gives back the new amounts and costs of the items in stock.
#     * `zipline` – Zipline is a Pythonic algorithmic trading library. It is an event-driven system that supports both backtesting and live trading.
#     * `QuantSoftware Toolkit` – Python-based open source software framework designed to support portfolio construction and management. It is built the QSToolKit primarily for finance students, computing students, and quantitative analysts with programming experience.
#     * `quantitative` – Quantitative finance, and backtesting library. Quantitative is an event driven and versatile backtesting library.
#     * `analyzer` – Python framework for real-time financial and backtesting trading strategies
#     * `bt` – bt is a flexible backtesting framework for Python used to test quantitative trading strategies.
#     * `backtrader` – Python Backtesting library for trading strategies
#     * `pybacktest` – Vectorized backtesting framework in Python / pandas, designed to make your backtesting easier. It allows users to specify trading strategies using full power of pandas, at the same time hiding all boring things like manually calculating trades, equity, performance statistics and creating visualizations. Resulting strategy code is usable both in research and production setting.
#     * `pyalgotrade` – PyAlgoTrade is an event driven algorithmic trading Python library. Although the initial focus was on backtesting, paper trading is now possible
#     * `tradingWithPython` – A collection of functions and classes for Quantitative trading
#     * `pandas_talib` – A Python Pandas implementation of technical analysis indicators
#     * `algobroker` – This is an execution engine for algo trading. The idea is that this python server gets requests from clients and then forwards them to the broker API.
#     * `finmarketpy` – finmarketpy is a Python based library that enables you to analyze market data and also to backtest trading strategies using a simple to use API, which has prebuilt templates for you to define backtest.
# 
# * Risk Analysis
# 
#     * `pyfolio` – pyfolio is a Python library for performance and risk analysis of financial portfolios. It works well with the Zipline open source backtesting library.
#     * `empyrical` – Common financial risk and performance metrics. Used by zipline and pyfolio.
#     * `finance` – Financial Risk Calculations. Optimized for ease of use through class construction and operator overload.
#     * `qfrm` – Quantitative Financial Risk Management: awesome OOP tools for measuring, managing and visualizing risk of financial instruments and portfolios.
#     * `visualize-wealth` – A library built in Python to construct, backtest, analyze, and evaluate portfolios and their benchmarks.
#     * `VisualPortfolio` – This tool is used to visualize the performance of a portfolio
# 
# * Time Series
# 
#     * `ARCH` – ARCH and other tools for financial econometrics in Python
#     * `statsmodels` – Python module that allows users to explore data, estimate statistical models, and perform statistical tests.
#     * `dynts` – A statistic package for python with emphasis on time series analysis. Built around numpy, it provides several back-end time series classes including R-based objects via rpy2.
# 
