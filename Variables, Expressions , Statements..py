#Variables, Expressions, Statements.

## Print hello world on the screen.
print("Hello World")
 
#Values: A value is a chunk of data. It is a basic thing that a program works with.
# Eg., 1, 2, 'Hello World'

#Types: Values are of different types. 1 is a number, 'Hello World' is string.

type(1) # integer type.
type('Hello, World!') #String type.
type(3.2) # floating point number type.
type('17') # string type.
type("23") # string type.

#Variables: A variabele is a name that refers to a value.
# An assignment statement creates new variables.

message = 'Now we are going to do something new'

n = 23
pi = 3.1417

#Type of the variable is the type of the value that it refers to.

type(message) # str
type(n) #int
type(pi) #float.

# Identifier: An identifier is a name used to idenjtify a python object-variable, module, function, object, Class.
# Rules for defining identifiers-
  # identifilers cannot be keywords.
  # identifiers can contain (a-z), (A-Z), (0-9), or (_) underscore character.
  # identifiers cannot start with a number.
  # identifiers cannot contain special symbols($,@, !, etc)
  # identifiers are case sensitive - var_1 is different from Var_1

# Keywords: Keywords are reserved words in python. Keywords can only be used for specific  purposed in python
# which are fixed.

## print all keywords of python.
import keyword
print(keyword.kwlist)

x1 = 3 # valid identifier.

 # 1x = 4 , invalid identifier because it starts with number.

total_marks = 100 #valid identifier with underscore.

 ## Variable Naming best practices.
  # start variable with lower case.
  # Use underscore for readabilty.
  # Make variable names understandable in context

total_score = 100 #clear.
#total_score_in_match = 200
ts = 100 # unclear.

#Operators and Operands.
# Operators are special symbols used to represent operations such as addition, multiplication.
# An operator is applied to values . The values that an operator is applied to are called operands
# +, -, %, / etc are a few operators in python.

2+3
x = 2
y = 3
print(x+ 2*y)

##Expressions and Statements
 # An expression is a combination of values, variables and operators.
 # A value or a variable all by itself is also considered and expression.
 # The following are legal ecpressions:
23
x
x+23

 # A statement is a unit of code that hte python in interpreter can execute
 # We had looked at assignment statement earlier.
 # Technically, an expression is also a statement.
 # Main differenceL An expression has a value but a statement does not.

number_of_days_in_week = 7
