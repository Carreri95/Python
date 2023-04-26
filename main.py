# coding: utf-8 

from first_code.hello_world import printHelloWorld
from operators.operators import add
from operators.operators import subtraction
from operators.operators import division
from operators.operators import multiplication
import operators.operators as op
printHelloWorld()

print(add(1.5, 1.6))
print(subtraction(2, 1))
print(division(10, 2))
print(multiplication(10, 2))
print(op.rest(10, 6))