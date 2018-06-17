#!/usr/bin/env python3

from read_vtk import read_vtk
from line_in_3d import line_in_z_3d
import matplotlib.pyplot as plt

def va():
    print("vtk analysis")
    fname = 'sample.vtk'
    tmpvtk = read_vtk(fname)
    grid = tmpvtk[0]
    spc = tmpvtk[1]
    org = tmpvtk[2]
    dens = tmpvtk[3]
    dens_1d = line_in_z_3d(dens,grid,13,13)
    plt.plot(dens_1d,'ro')
    plt.show()
    print('end')

def main():
    try:
        va()
    except:
        print("Failed.")

if __name__ == '__main__':
    main()
