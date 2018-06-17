#read_vtk.py

def read_vtk(fn):
    with open(fn,'r') as f:
        #print('reading', fn)
        grid = []
        spc = []
        org = []
        dens = []
        zvel = []
        xvel = []
        yvel = []
        mark_dens = 0
        mark_zvel = 0
        mark_xvel = 0
        mark_yvel = 0
        datasize = 0
        for line in f:
            if line.startswith('DIMENSIONS'):
                count = 1
                for word in line.split():
                    if count > 1:
                        grid.append(int(word))
                    count += 1
                if count > 1:
                    grid[0] -= 1
                    grid[1] -= 1
                    grid[2] -= 1
                    datasize = grid[0]*grid[1]*grid[2]
            if line.startswith('SPACING'):
                count = 1
                for word in line.split():
                    if count > 1:
                        spc.append(float(word))
                    count += 1
            if line.startswith('ORIGIN'):
                count = 1
                for word in line.split():
                    if count > 1:
                        org.append(float(word))
                    count += 1
            if line.startswith('SCALARS DENSITY'):
                mark_dens = 1
                count = -2
            if mark_dens == 1:
                count += 1
                if count > 0 & count < datasize+1:
                    for word in line.split():
                        dens.append(float(word))
                if count == datasize:
                    mark_dens = 0
            '''
            if line.startswith('SCALARS XVEL'):
                mark_xvel = 1
                count = -2
            if mark_xvel == 1:
                count += 1
                if count > 0 & count < datasize+1:
                    for word in line.split():
                        xvel.append(float(word))
                if count == datasize:
                    mark_xvel = 0
            if line.startswith('SCALARS YVEL'):
                mark_yvel = 1
                count = -2
            if mark_yvel == 1:
                count += 1
                if count > 0 & count < datasize+1:
                    for word in line.split():
                        yvel.append(float(word))
                if count == datasize:
                    mark_yvel = 0
            if line.startswith('SCALARS ZVEL'):
                mark_zvel = 1
                count = -2
            if mark_zvel == 1:
                count += 1
                if count > 0 & count < datasize+1:
                    for word in line.split():
                        zvel.append(float(word))
                if count == datasize:
                    mark_zvel = 0
        return [grid, spc, org, dens, zvel, xvel, yvel]
        '''
        return [grid, spc, org, dens]

