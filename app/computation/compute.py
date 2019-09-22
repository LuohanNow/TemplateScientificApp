from numpy import exp, cos, linspace, arctan, nditer, zeros
import matplotlib.pyplot as plt, mpld3
#import bokeh.plotting as plt
#from bokeh.embed import components
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
    fig, ax = plt.subplots(figsize=(6,4)) # needed to avoid adding curves in plot
    ax.plot(t, u, label ='damped_sin')
    ax.plot(t, z, label ='arctg(x) + b', color = 'red')
    ax.grid()
    ax.set_title('A=%g, b=%g, w=%g' % (A, b, w))
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()
    html_text = mpld3.fig_to_html(fig)
    #plt.set_ylim(-10,10)
    return html_text

if __name__ == '__main__':
    print(compute(1, 0.1, 1, 20))


#TOOLS = "pan, wheel_zoom, box_zoom, reset, save, box_select, lasso_select"
#    p = plt.figure(
#        title = 'A=%g, b=%g, w=%g' % (A, b, w),
#        tools = TOOLS,
#        x_axis_label ="X",
#        y_axis_label = "Y")
#        #y_axis_type ="log", y_range=[0.0001, 10*11]
#        #plot_width/height, toolbar_location, h/v_symmentry, min_border, responsive, outline_line_color
#
#    p.line(t, u, legend ='damped_sin', line_width = 2)
#    p.line(t, z, legend ='arctg(x) + b', line_width = 2, line_color = 'red')
#
#    script, div = components(p)
#
#    head = """
#<link rel="stylesheet"
#href="http://cdn.pydata.org/bokeh/release/bokeh-1.3.4.min.css"
#type="text/css" />
#<script type="text/javascript"
#src="http://cdn.pydata.org/bokeh/release/bokeh-1.3.4.min.js">
#</script>
#<script type="text/javascript">
#Bokeh.set_log_level("info");
#</script>
#"""
#
#    return head, script, div