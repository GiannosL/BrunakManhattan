import numpy as np
import matplotlib.pyplot as plt


def beta_plot(df_a, df_b, snps_of_interest, palette):
    # subset data
    df_a = df_a[df_a['snp'].isin(snps_of_interest)]
    df_b = df_b[df_b['snp'].isin(snps_of_interest)]

    x_lim = df_b['beta'].max()
    x_lim = x_lim if x_lim > df_b['beta'].max() else df_b['beta'].max()
    x_lim += x_lim*0.1
    
    #
    points = np.linspace(-2, 2, 1000)

    # plotting
    plt.scatter(df_a['beta'], df_b['beta'], c=palette['normal'], edgecolors='black')
    plt.plot(points, points, c='#817F82')

    plt.ylim((-x_lim, x_lim))
    plt.xlim((-x_lim, x_lim))
