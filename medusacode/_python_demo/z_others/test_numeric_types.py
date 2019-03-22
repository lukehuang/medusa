#!/usr/bin/env python
# coding:utf-8


"""
数值类型
"""
"""
Numeric Types — int, float, long, complex

There are four distinct numeric types: 
    plain integers, long integers, floating point numbers, complex numbers. 
    (In addition, Booleans are a subtype of plain integers.) 

int
    Plain integers (also just called integers) are implemented using long in C, 
    which gives them at least 32 bits of precision 
    (sys.maxint is always set to the maximum plain integer value for the current platform, the minimum value is -sys.maxint - 1). 

long
    Long integers have unlimited precision. 

float
    Floating point numbers are usually implemented using double in C; 
    information about the precision and internal representation of floating point numbers for the machine 
    on which your program is running is available in sys.float_info. 

complex
    Complex numbers have a real and imaginary part, which are each a floating point number. 
    To extract these parts from a complex number z, use z.real and z.imag. 
"""
