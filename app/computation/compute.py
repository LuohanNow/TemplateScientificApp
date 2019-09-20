from numpy import exp, cos, linspace, arctan, nditer, zeros
import matplotlib.pyplot as plt
import os, time, glob

def z_func(x, b):
    return arctan(x) + b

def damped_vibrations(t, A, b, w):
    return A*exp(-b*t)*cos(w*t)

def compute(A, b, w, T, resolution=500):
    """Return filename of plot of the damped_vibration function."""
    t = linspace(0, T, resolution+1)
    #x = linspace(Xbeg, Xend, (Xend-Xbeg)/dx + 1)
    u = damped_vibrations(t, A, b, w)
    z = z_func(t, b)
    plt.figure() # needed to avoid adding curves in plot
    plt.plot(t, u, label ='damped_sin')
    plt.plot(t, z, label ='arctg(x) + b', color = 'red')
    plt.grid()
    plt.title('A=%g, b=%g, w=%g' % (A, b, w))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    #plt.ylim(-10,10)

    if not os.path.isdir('app/static'):
        os.mkdir('app/static')
    else:
        for filename in glob.glob(os.path.join('app/static', '*.png')):
            os.remove(filename)
    plotfile = os.path.join('app/static', str(time.time()) + '.png')
    plt.savefig(plotfile)
    plotfile = plotfile[4:]
    return plotfile

if __name__ == '__main__':
    print(compute(1, 0.1, 1, 20))
