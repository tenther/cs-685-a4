#!/usr/bin/env python

# Computer Science 685 Assignment 3
# Paul McKerley (G00616949)

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import pdb 

X_AXIS = 0
Y_AXIS = 1
Z_AXIS = 2

def deg2rad(deg):
    return deg/180.0*np.pi

def make_axis_rotation_matrix(axis, theta):
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)

    mat = np.zeros((3,3))
    if axis == X_AXIS:
        mat[0,0] = 1.0
        mat[1,1] = mat[2,2] = cos_theta
        mat[1,2] = -sin_theta
        mat[2,1] = sin_theta
    elif axis == Y_AXIS:
        mat[1,1] = 1.0
        mat[0,0] = mat[2,2] = cos_theta
        mat[2,0] = -sin_theta
        mat[0,2] = sin_theta
    elif axis == Z_AXIS:
        mat[2,2] = 1.0
        mat[0,0] = mat[1,1] = cos_theta
        mat[0,1] = -sin_theta
        mat[1,0] = sin_theta
    else:
        raise Exception("Unknown axis {}", axis)
    return mat

def project(X_w, R, T, K):
    # Create rigid body transformation matrix
    RB          = np.zeros(12).reshape((3,4))
    RB[:3,:3]   = R
    RB[:3,3:4] += T

    # Apply rigid body transformation and camera transformation to points in vector
    X_c         = np.matmul(K, np.matmul(RB, X_w))

    # Normalize z coordinate and remove from vectors to get
    # (x,y) coordinates.
    return (X_c / X_c[:,2:,0:])[:,:2].reshape(-1,2)
    
def main():
    coordinates = []
    count = 0
    for x in range(2):
        for y in range(2):
            for z in range(2):
                 count += 1
                 coordinates.extend([x,y,z,1])
    X_w = np.array(coordinates).reshape((count,4,1))

    # [0, 0, 0]
    # [0, 0, 1],
    # [0, 1, 0],
    # [0, 1, 1],
    # [1, 0, 0],
    # [1, 0, 1],
    # [1, 1, 0],
    # [1, 1, 1]

    line_indexes = [
        (1,0),
        (0,4),
        (0,2),
        (1,3),
        (1,5),
        (4,5),
        (4,6),
        (2,3),
        (2,6),
        (3,7),
        (6,7),
        (5,7),
        ]

    pdb.set_trace()
    K   = np.array([800.0, 0.0, 250.0, 0.0, 800.0, 250.0, 0.0, 0.0, 1.0]).reshape((3,3))
    R   = make_axis_rotation_matrix(X_AXIS, deg2rad(20))
    T   = np.array([0.0, 0.0, 5.0]).reshape((3,1))
    X_c = project (X_w, R, T, K)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.axis((0, 500, 500, 0))
    ax.scatter(x=X_c[:,0], y=(X_c[:,1]), c='r')
    line_coords = [([X_c[p][0] for p in line],[X_c[p][1] for p in line]) for line in line_indexes]
    for line in line_coords:
        ax.add_line(Line2D(line[0], line[1]))
    ax.set_aspect('equal')
    plt.savefig('hw3_perspective_projection.png')
    plt.show()

    return

if __name__=='__main__':
    main()
    
