import numpy as np
import pandas as pd
from app.computation.visualization import visualize, table_to_html

def z_func(x, b):
    return np.arctan(x) + b

def damped_vibrations(t, A, b, w):
    return A*np.exp(-b*t)*np.cos(w*t)

def compute(A, b, w, T, resolution=500):
    """Return filename of plot of the damped_vibration function."""
    t = np.linspace(0, T, resolution+1)
    #x = linspace(Xbeg, Xend, (Xend-Xbeg)/dx + 1)
    u = damped_vibrations(t, A, b, w)
    z = z_func(t, b)

    html_text = visualize(t, u, z, A, b, w)
    df1 = table_to_html(t, u)
    return html_text, df1

if __name__ == '__main__':
    print(compute(1, 0.1, 1, 20))
