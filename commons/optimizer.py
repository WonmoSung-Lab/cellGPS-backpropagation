import numpy as np
from scipy.optimize import minimize

from commons.backpropagation import CalculateLoss
from commons.utils import *


def single_cellGPS(A, LORs, N, k, knots, lambda0, dmax, options={'maxiter': 2000, 'disp': True}):
    '''
    input:
    - A: initial coefficients, usually np.zeros((3, N))
    - LORs: detected LORs, shape: (-1, 8)
    - N: number of basis functions
    - k: degree of spline, usually 3
    - knots: knots
    
    output
    - optimized A
    '''
    if len(knots) != N + k + 1:
        raise ValueError('knots, N, k are not valid')
    
    sorted_indices = LORs[:, 3].argsort()
    LORs = LORs[sorted_indices]
    
    P1, v, times = get_P1_v_times(LORs)
    calculateLoss = CalculateLoss(k, knots, times, P1, v, dmax, lambda0)
    result = minimize(lambda A: calculateLoss.get_val_and_grad(A, 1.0), A, method='BFGS', jac=True, options=options)
    
    return result.x


