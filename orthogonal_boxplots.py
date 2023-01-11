import matplotlib.pyplot as plt
import numpy as np

def ortogonal_boxplot(x, y, facecolor='white', edgecolor='black', tickness=1, plot_data=True, ):


    # Create a figure and axes
    fig, ax = plt.subplots()

    x= list(x)
    y= list(y)
    # sort the data
    x = sorted(x)
    y =sorted(y)
    
    # calculate quartiles
    x_q1, x_q2, x_q3 = np.percentile(x, [25,50,75])
    y_q1, y_q2, y_q3 = np.percentile(y, [25,50,75])

    # Calculate IQR
    x_iqr = x_q3 - x_q1
    y_iqr = y_q3 - y_q1

    
    # Draw box
    rect = plt.Rectangle((x_q1, y_q1), x_q3-x_q1, y_q3 - y_q1, facecolor=facecolor, lw=tickness, alpha=1,edgecolor=edgecolor)
    ax.add_patch(rect) 

    # whiskers
    ax.plot([x[0], x[-1]], [y_q2, y_q2], lw=tickness, color='black')
    ax.plot([x_q2,x_q2],[y[0], y[-1]],  lw=tickness, color='black')

    # Draw whiskers
    for x_ in [x[0], x[-1]]:
        ax.plot([x_, x_], [y_q2 - 0.1* y_iqr, y_q2+ 0.1* y_iqr], lw=tickness, color='black')
    for x_ in [y[0], y[-1]]:
        ax.plot([x_q2 -0.1 * x_iqr, x_q2+ 0.1* x_iqr],[x_, x_], lw=tickness, color='black')

    # Draw dots
    if plot_data:
    
        ax.plot(x, np.ones_like(x) * y_q2, 'o', markersize=6, color='red', alpha=.5)
        ax.plot(np.ones_like(y) * x_q2, y, 'o', markersize=6, color='red', alpha=.5)

    return ax
