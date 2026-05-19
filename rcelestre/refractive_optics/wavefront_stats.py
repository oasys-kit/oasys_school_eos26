def wavefront_stats(wavefront):

    nx, ny = wavefront.mesh.nx, wavefront.mesh.ny
    range_x, range_y = wavefront.mesh.xFin - wavefront.mesh.xStart, wavefront.mesh.yFin - wavefront.mesh.yStart
    dx, dy = range_x/(wavefront.mesh.nx -1), range_y/(wavefront.mesh.ny -1)
    
    print('\n >>> wavefront parameters:')
    print(f'\tNx = {nx}, Ny = {ny}')
    print(f'\tdx = {dx*1e6:.3f} µm, dy = {dy*1e6:.3f} µm')
    if range_x >= 0.7e-3 or range_y >= 0.7e-3:
        print(f'\trange x = {range_x*1e3:.3f} mm, range y = {range_y*1e3:.3f} mm')
    else:
        print(f'\trange x = {range_x*1e6:.3f} µm, range y = {range_y*1e6:.3f} µm')

    print(f'\tRx = {wavefront.Rx:.6e} m, Ry = {wavefront.Ry:.6e} m\n')

wavefront_stats(in_object_1._SRWData__srw_wavefront)