import numpy as np
from scipy.interpolate import BSpline
from commons.utils import get_v


def diff_ys(s):
    return s[:, :-1] - s[:, 1:]

# def objf2D(s, T, P1, P2, t, dmax, lambda0):
#     n = len(t)
#     s = s.reshape((2, -1))
#     m = s.shape[1] # s.shape = 2* n

#     v = get_v(P1=P1, P2=P2)
    
#     # degree of B spline
#     k = 3
#     # knots
#     Ts = np.r_[[0]*k, T, T[-1]*k] 
    
#     # coefficients
#     s_x = s[0,]
#     s_y = s[1,]
    
#     spl_x = BSpline(Ts, s_x, k) # t, c, k
#     spl_y = BSpline(Ts, s_y, k)

#     M_x = spl_x(t).reshape((-1, len(t)))
#     M_y = spl_y(t).reshape((-1, len(t)))

#     M = np.concatenate([M_x, M_y], axis=0)

#     MP = M - P1
#     dMPv = np.multiply(MP, v).sum(axis=0)
#     dMPMP = np.multiply(MP, MP).sum(axis=0)
#     df = dMPMP - np.multiply(dMPv, dMPv)

#     dmax_2 = np.repeat(dmax**2, len(df))
#     D = np.mean(np.minimum(dmax**2, df))

#     s_diff = diff_ys(s)
#     sum_s_diff2 = np.multiply(s_diff, s_diff).sum(axis=0)

#     R = np.mean(sum_s_diff2)

#     J = D + lambda0 * R

#     return J

def objf3D(k, s, knots, P1, P2, t, dmax, lambda0):
    n = len(t)
    s = s.reshape((3, -1))
    m = s.shape[1] # s.shape = 3*73 

    v = get_v(P1=P1, P2=P2)
    
    # coefficients
    s_x = s[0,]
    s_y = s[1,]
    s_z = s[2,]


    spl_x = BSpline(knots, s_x, k) 
    spl_y = BSpline(knots, s_y, k)
    spl_z = BSpline(knots, s_z, k) 

    M_x = spl_x(t).reshape((-1, len(t)))
    M_y = spl_y(t).reshape((-1, len(t)))
    M_z = spl_z(t).reshape((-1, len(t)))

    M = np.concatenate([M_x, M_y, M_z], axis=0)

    MP = M - P1
    dMPv = np.multiply(MP, v).sum(axis=0)
    dMPMP = np.multiply(MP, MP).sum(axis=0)
    df = dMPMP - np.multiply(dMPv, dMPv)

    dmax_2 = np.repeat(dmax**2, len(df))
    D = np.mean(np.minimum(dmax**2, df))

    s_diff = diff_ys(s)
    sum_s_diff2 = np.multiply(s_diff, s_diff).sum(axis=0)

    R = np.mean(sum_s_diff2)

    J = D + lambda0 * R

    return J