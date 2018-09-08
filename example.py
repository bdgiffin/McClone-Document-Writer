# example.py

import os
import matplotlib.pyplot as pplot
from math import *

L = 20.0 # ft (beam length)
w = 1.0  # kips/ft (constant load)
N = 100  # number of line segements
fnt = 10 # figure font size

x=[L*i for i in range(0,N+1)]
p=[w for i in range(0,N+1)]
v=[L*i/N for i in range(0,N+1)]
m=[w-pow(L*i/N,2) for i in range(0,N+1)]

# plot load
pplot.figure(figsize=(5, 2))
pplot.plot(x,p,'-', color='m', linewidth=2)
pplot.xticks(fontsize=fnt)
pplot.xlabel('x (ft)', fontsize=fnt)
pplot.yticks(fontsize=fnt)
pplot.ylabel('Moment (kip-in)', fontsize=fnt)
pplot.savefig("load_diagram.pdf")
pplot.close()

# plot shear
pplot.figure(figsize=(5, 2))
pplot.plot(x,v,'-', color='b', linewidth=2)
pplot.xticks(fontsize=fnt)
pplot.xlabel('x (ft)', fontsize=fnt)
pplot.yticks(fontsize=fnt)
pplot.ylabel('Shear force (kip-in)', fontsize=fnt)
pplot.savefig("shear_diagram.pdf")
pplot.close()

# plot moment
pplot.figure(figsize=(5, 2))
pplot.plot(x,m,'-', color='r', linewidth=2)
pplot.xticks(fontsize=fnt)
pplot.xlabel('x (ft)', fontsize=fnt)
pplot.yticks(fontsize=fnt)
pplot.ylabel('Moment (kip-in)', fontsize=fnt)
pplot.savefig("moment_diagram.pdf")
pplot.close()

# generate document
os.system('pdflatex document.tex')
