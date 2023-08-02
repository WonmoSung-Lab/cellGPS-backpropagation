import numpy as np
from scipy.optimize import minimize

from commons.lossWithGrad import CalculateLoss
from commons.utils import *


def single_cellGPS(A, LORs, N, k, knots, lambda0, dmax, options={'maxiter': 2000, 'disp': True}):
    '''
    input:
    - A: 초기값, 보통 np.zeros((3, N))
    - LORs: 관측된 LORs, shape: (관측된 LOR 개수, 8)
    - N: control point의 개수
    - k: spline의 차수, cubic의 경우에는 3
    - knots: knots
    
    output
    - optimized a0
    '''
    if len(knots) != N + k + 1:
        raise ValueError('knots, N, k are not valid')
    
    sorted_indices = LORs[:, 3].argsort()
    LORs = LORs[sorted_indices]
    
    P1, v, times = get_P1_v_times(LORs)
    calculateLoss = CalculateLoss(k, knots, times, P1, v, dmax, lambda0)
    result = minimize(lambda A: calculateLoss.get_val_and_grad(A, 1.0), A, method='BFGS', jac=True, options=options)
    
    return result.x


