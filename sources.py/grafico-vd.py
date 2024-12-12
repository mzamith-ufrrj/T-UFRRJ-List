#!/opt/anaconda/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys
import pandas as pd
if __name__ == "__main__":
    columns = ['timestep', 'samples', 'flow', 'density', 'velocity', 'lane0']
    df_p = pd.read_csv(sys.argv[1], names=columns, delimiter=';', header=None)
    df_f = pd.read_csv(sys.argv[2], names=columns, delimiter=';', header=None)

    X_p = df_p['density'] * 133
    Y_p = df_p['velocity'] * 1.5 * 3.6
    X_f = df_f['density'] * 133
    Y_f = df_f['velocity'] * 1.5 * 3.6

    fig, ax =  plt.subplots(figsize=(12, 8))

    #ax.plot(xcub1, ycub1, '-', label=r'$ax^3+bx^2+cx$', c="red")
    #ax.plot(xcub2, ycub2, '-', label=r'$ax^3+bx^2+cx+d$', c="green")
    ax.plot(X_f, Y_f, '.', label='Photo', c="red")
    ax.plot(X_p, Y_p, '.', label='Fixed', c="green")

    #label = r'$\frac{1}{{{{}}}x^2 + {{{}}}$'.format(XAdust1[0], XAdust1[1] )

    plt.legend()
    #print(plabel)
    plt.title('Densidade por velocidade')
    #plt.ylim([-0.1, 1.2])
    #plt.xlim([min(Xi)-10,  max(Xi)+10])
    plt.grid()
    #filename = 'inter-Runge-{:03}.eps'.format(points+1)
    #plt.savefig(filename)
    #print('Arquivo: ', filename, " salvo")
    plt.show()
