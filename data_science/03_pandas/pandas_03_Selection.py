#!/usr/bin/env python
# coding:utf-8


from pandas_02_Viewing_Data import *

print '-----------------------------------------------------------------------------'
"""
                   A         B         C         D
2017-01-01  0.406287  1.158293  0.971685  0.405280
2017-01-02 -0.527079 -1.370936  0.535477 -1.087935
2017-01-03 -0.853528 -0.101003 -1.815336  1.280109
2017-01-04  0.432196 -1.274989 -2.872778  0.932454
2017-01-05  1.193823 -0.469238  0.100933  0.068175
2017-01-06  1.125678 -2.295941  1.071525  0.859002
"""
print '-----------------------------------------------------------------------------'
# Getting
# Selecting a single column, which yields a Series, equivalent to df.A:
print df.get('A')
"""
2017-01-01    0.406287
2017-01-02   -0.527079
2017-01-03   -0.853528
2017-01-04    0.432196
2017-01-05    1.193823
2017-01-06    1.125678
Freq: D, Name: A, dtype: float64
"""
print '-----------------------------------------------------------------------------'
# Getting
# Selecting via [], which slices the rows.
print df[0:3]
"""
                   A         B         C         D
2017-01-01  0.406287  1.158293  0.971685  0.405280
2017-01-02 -0.527079 -1.370936  0.535477 -1.087935
2017-01-03 -0.853528 -0.101003 -1.815336  1.280109
"""
print '-----------------------------------------------------------------------------'
# Selection by Label
# For getting a cross section using a label:
print df.loc[dates[0]]
"""
A    0.406287
B    1.158293
C    0.971685
D    0.405280
Name: 2017-01-01 00:00:00, dtype: float64
"""
print '-----------------------------------------------------------------------------'
# Selection by Label
# Selecting on a multi-axis by label:
print df.loc[:, ['A', 'B']]
"""
                   A         B
2017-01-01  0.406287  1.158293
2017-01-02 -0.527079 -1.370936
2017-01-03 -0.853528 -0.101003
2017-01-04  0.432196 -1.274989
2017-01-05  1.193823 -0.469238
2017-01-06  1.125678 -2.295941
"""
print '-----------------------------------------------------------------------------'
# Selection by Label
# Showing label slicing, both endpoints are included:
print df.loc['20170102':'20170104', ['A', 'B']]
"""
                   A         B
2017-01-02 -0.527079 -1.370936
2017-01-03 -0.853528 -0.101003
2017-01-04  0.432196 -1.274989
"""
print '-----------------------------------------------------------------------------'
# Selection by Label
# Reduction in the dimensions of the returned object:
print df.loc['20170102', ['A', 'B']]
"""
A   -0.527079
B   -1.370936
Name: 2017-01-02 00:00:00, dtype: float64
"""
print '-----------------------------------------------------------------------------'
# Selection by Label
# For getting a scalar value:
print df.loc[dates[0], 'A']
"""
0.406286816852
"""
# Selection by Label
# For getting fast access to a scalar (equivalent to the prior method):
print df.at[dates[0], 'A']
"""
0.406286816852
"""
print '-----------------------------------------------------------------------------'
# Selection by Label
# Select via the position of the passed integers:
print df.iloc[0]
"""
A    0.406287
B    1.158293
C    0.971685
D    0.405280
Name: 2017-01-01 00:00:00, dtype: float64
"""
# By integer slices, acting similar to numpy/python:
print df.iloc[3:5, 0:2]
"""
                   A         B
2017-01-04  0.432196 -1.274989
2017-01-05  1.193823 -0.469238
"""
# For slicing rows explicitly:
print df.iloc[1:3, :]
"""
                   A         B         C         D
2017-01-02 -0.527079 -1.370936  0.535477 -1.087935
2017-01-03 -0.853528 -0.101003 -1.815336  1.280109
"""
# For slicing columns explicitly:
print df.iloc[:, 1:3]
"""
                   B         C
2017-01-01  1.158293  0.971685
2017-01-02 -1.370936  0.535477
2017-01-03 -0.101003 -1.815336
2017-01-04 -1.274989 -2.872778
2017-01-05 -0.469238  0.100933
2017-01-06 -2.295941  1.071525
"""
# By lists of integer position locations, similar to the numpy/python style:
print df.iloc[[1, 2, 4], [0, 2]]
"""
                   A         C
2017-01-02 -0.527079  0.535477
2017-01-03 -0.853528 -1.815336
2017-01-05  1.193823  0.100933
"""
# For getting a value explicitly:
print df.iloc[0, 0]
"""
0.406286816852
"""
# For getting fast access to a scalar (equivalent to the prior method):
print df.iat[0, 0]
"""
0.406286816852
"""
print '-----------------------------------------------------------------------------'
