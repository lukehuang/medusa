#!/usr/bin/env python
# coding:utf-8

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator
from matplotlib import cm
from matplotlib import pyplot
import numpy

figure = pyplot.figure()
ax = figure.gca(projection='3d')
x, t = numpy.meshgrid(
    numpy.array(range(25))/24.0,
    numpy.arange(0, 575.5, 0.5)/575*17*numpy.pi-2*numpy.pi
)
p = (numpy.pi/2)*numpy.exp(-t/(8*numpy.pi))
u = 1-(1-numpy.mod(3.6*t, 2*numpy.pi)/numpy.pi)**4/2
y = 2*(x**2-x)**2*numpy.sin(p)
r = u*(x*numpy.sin(p)+y*numpy.cos(p))
surf = ax.plot_surface(
    r*numpy.cos(t),
    r*numpy.sin(t),
    u*(x*numpy.cos(p)-y*numpy.sin(p)),
    rstride=1,
    cstride=1,
    cmap=cm.gist_rainbow_r,
    linewidth=0,
    antialiased=True)
pyplot.show()
