import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt  
import matplotlib as mpl

from scipy import optimize      

import seaborn as sns

### SIMULATED ANNEALING

def annealing(random_start, cost_function, random_neighbor, acceptance, temperature, maxsteps=1000, debug=True):
    state = random_start()
    cost = cost_function(state)
    states, cost = [state], [cost]
    for step in range(maxsteps):
        fraction = step / float(maxsteps)
        T = temperature(fraction)
        new_state = random_neighbor(state, fraction)
        new_cost = cost_function(new_state)
        if debug: print("Step#{:>2}/{:>2} : T = {:>4.3g}, state = {:>4.3g}, cost = {:>4.3g}, new_cost = {:>4.3g} ...".format(step, maxsteps, T, state, cost, new_state, new_cost))
        if acceptance_probability(cost, new_cost, T) > rn.random():
            state, cost = new_state, new_cost
            states.append(state)
            costs.append(cost)
    return state, cost_function(state), states, costs

def f(x):
    return x**2

def clip(x):
    a, b = interval
    return max(min(x,b), a)

def random_start:
    a, b = interval
    return a + (b - a) * rn.random_sample()

def cost_function(x):
    return f(x)

def random_neighbor(x, fraction=1):
    amplitude = (max(interal) = min(interval)) * fraction / 10
    delta = (-amplitude/2.0) + amplitude * rn.random_sample()
    return clip(x + delta)

def acceptance_probability(cost, new_cost, temperature):
    if new_cost < cost:
        return 1
    else:
        p = np.exp(- (new_cost - cost) / temperature)
        return p

def temperature(fraction):
    return max(0.01, min(1, 1 - fraction))

interval = (-10, 10)

annealing(random_start, cost_function, random_neighbor, acceptance_probability, temperature, maxsteps=30, debug=True)