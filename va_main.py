#!/usr/bin/env python3

from read_vtk import read_vtk
from line_in_3d import line_in_z_3d
from plot_vtk import plot_dens_1D, multi_plot_dens_1D
import os, sys, getopt

def va(indir,outdir):
    print("vtk analysis")
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    '''
    files = [f for f in os.listdir(indir) if os.path.isfile(os.path.join(indir,f))]
    plot_dens_1D(indir,files[0],outdir)
    '''
    multi_plot_dens_1D(indir,outdir)
    print("end")

def main(argv):
    inputdir = ''
    outputdir = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["idir=","odir="])
    except getopt.GetoptError:
        print ("test.py -i <inputdir> -o <outputdir>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ("test.py -i <inputdir> -o <outputdir>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputdir = arg
        elif opt in ("-o", "--ofile"):
            outputdir = arg
            print ("Input dir is %s" % inputdir)
            print ("Output dir is %s" % outputdir)
    try:
        va(str(inputdir),str(outputdir))
    except:
        print("Failed.")

if __name__ == '__main__':
    main(sys.argv[1:])
