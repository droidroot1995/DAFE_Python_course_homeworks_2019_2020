import numpy as np
import matplotlib.pyplot as plt

def euler(fn, а0, tau, T):
    n_t = int(round(T/tau))
    fn_ = lambda t, ar: np.asarray(fn(t, ar))
    t = np.linspace(0, n_t*tau, n_t+1)
    ar = np.zeros((n_t+1, len(a0)))
    ar[0] = np.array(a0)
    for n in range(n_t):
        ar[n+1] = ar[n] + tau*fn_(t[n], ar[n])
    return ar, t
  
def implicit_euler(T, a0, tau, fn):
    from scipy import optimize
    n_t = int(round(T/tau))
    fn_ = lambda t, ar: np.asarray(fn(t, ar))
    t = np.linspace(0, n_t*tau, n_t+1)
    ar = np.zeros((n_t+1, len(a0)))
    ar[0] = np.array(a0)

    def fn2(z, t, v):
        return z - tau*fn_(t, z) - v
    for n in range(n_t):
        ar[n+1] = optimize.fsolve(fn2, ar[n], args=(t[n], ar[n]))
    return ar, t  
    
