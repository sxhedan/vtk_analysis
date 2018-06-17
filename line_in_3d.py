#line_in_3d.py

def line_in_z_3d(state,grid,gx,gy):
    state_1d = []
    for gz in range(grid[2]):
        state_1d.append(state[(gz*grid[1]+gy)*grid[0]+gx])
    return state_1d
