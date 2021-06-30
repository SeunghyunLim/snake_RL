# © 2021 Bongsub Song <doorebong@gmail.com>
# All right reserved
# Description : BRM snake robot python simulation script

from numpy.core.fromnumeric import reshape, shape
import os
import math
import numpy as np
import time

def radtodeg(rad):
    return rad * 180/math.pi

def degtorad(deg):
    return deg * math.pi/180



#Gait parameters
l_amp = 30 # lateral amplitude
l_phase = 150 # lateral phase
d_amp = 30 # dorsal amplitude
d_phase = 150 # dorsal phase
tau = 5 #
k = 1 # time slot variable

#Gait motion matirces
m_vertical = np.array([[1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0], 
                        [0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0]],np.float)

m_sinuous = np.eye(16)

def getMotionCol(M,i):
    return M[:,i].reshape(M.shape[0],1)


#Joint angle function
def P_vertical(slot):
    return np.array([[d_amp * math.cos(slot + degtorad(d_amp))],
                        [0],
                        [d_amp * math.cos(slot + 3 * degtorad(d_amp))],
                        [0],
                        [d_amp * math.cos(slot + 5 * degtorad(d_amp))],
                        [0],
                        [d_amp * math.cos(slot + 7 * degtorad(d_amp))],
                        [0],
                        [d_amp * math.cos(slot + 9 * degtorad(d_amp))],
                        [0],
                        [d_amp * math.cos(slot + 11 * degtorad(d_amp))],
                        [0],
                        [d_amp * math.cos(slot + 13 * degtorad(d_amp))],
                        [0],
                        [d_amp * math.cos(slot + 15 * degtorad(d_amp))],
                        [0]],np.float
)


#Select gait if we select vertical -> gait slot is 8.
t = 0
k = 0
G = np.zeros((16,1))
while True:
   
    P = P_vertical(k)
    m_k = getMotionCol(m_vertical,(k%8)).T
    g = np.round(np.diagonal((np.dot(P,m_k))),decimals=2)
    G = G + g

    print(G)
    time.sleep(0.3)

    t = t + 1
    k = (k + 1)