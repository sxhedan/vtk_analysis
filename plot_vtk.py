#plot_vtk.py

from read_vtk import read_vtk
from line_in_3d import line_in_z_3d
import matplotlib.pyplot as plt
import os

def plot_dens_1D(indir,fn,outdir):
    inputfile = os.path.join(indir,fn)
    print("input: %s" % inputfile)
    tmpvtk = read_vtk(inputfile)
    grid = tmpvtk[0]
    dens = tmpvtk[3]
    gx = grid[0]//1
    gy = grid[1]//2
    dens1D = line_in_z_3d(dens,grid,gx,gy)
    plt.figure()
    plt.plot(dens1D,'ro')
    #outname = fn[:-4] + ".pdf"
    outname = fn[:-4] + ".png"
    outputfile = os.path.join(outdir,outname)
    print("output: %s" % outputfile)
    plt.savefig(outputfile)
    plt.close()

def multi_plot_dens_1D(indir,outdir):
    files = [f for f in os.listdir(indir) if os.path.isfile(os.path.join(indir,f))]
    for f in files:
        plot_dens_1D(indir,f,outdir)
