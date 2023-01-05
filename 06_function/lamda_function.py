'''
Functions are divided into two main parts:

1)build in function.
2)user defined function.
    -user defined function is divided into two parts
    1)lamda function(anonymous function)
    2)recursive function

Lambda Function
===============

Need of Funtion
---------------
1)single it is one line function,it has faster ecexution.
 [shorter the code,faster is exexution]
2)if there is need to pass a function as an argument to another
 function,then use lamba function to pass as an argument.


Function without name is called as anonymous function or
lambda funtion.

lamda function always returns result of the expression.

syntax for lamda function defination:
=======================================

var=lamda arguments:expression

to call lambda function
-----------------------
var (arguments)
'''

a=lambda x,y:x+y

res=a(20,30)

print("Addition is: ",res)

