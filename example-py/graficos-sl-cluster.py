#!/home/mzamith/Apps/anaconda3/bin/python
import matplotlib.pyplot as plt
import math
import numpy as np
import csv
import sys





def cluster(D_ST, V_ST, D_SL, F_SL, D_DA, F_DA, save, filename):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(D_ST, F_ST, color='blue',  linewidth=1)
    ax.plot(D_SL, F_SL, color='red',  linewidth=1)
    ax.plot(D_DA, F_DA, color='green',  linewidth=1)


    ax.set_xlabel('density [v/km]')
    ax.set_ylabel('frenquency (%)')


    ax.legend(['standard', 'slow', 'daring'])

    plt.xlim([0, 135])
    #plt.ylim([0, 3600])
    plt.xticks(np.arange(0, 136, 10.0))
    #plt.yticks(np.arange(0, 3600, 500.0))
    plt.title('Velocities adjustment frequency')
    plt.grid(True)
    if save == 1:
        plt.savefig(filename, format='eps')
    else:
        plt.show()



def loadData(filename, w):
    F = []
    D = []

    print('Lendo arquivo:', filename, w)
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            d = float(row[0]) * w
            f = float(row[3])
            D.append(d)
            F.append(f)

    return D, F

if __name__ == "__main__":
    filename_ST = 'cluster.adjusted.SL-STANDARD-HR-1.5.csv'
    filename_SL = 'cluster.adjusted.SL-SLOW-HR-1.5.csv'
    filename_DA = 'cluster.adjusted.SL-DARING-HR-1.5.csv'
    cluster_filename  = 'cluster.eps'
    weight_density    =  133
    save = 1

    print('Graficos')
    D_ST, F_ST = loadData(filename_ST, weight_density)
    D_SL, F_SL = loadData(filename_SL, weight_density)
    D_DA, F_DA = loadData(filename_DA, weight_density)

    print('Grafico: fluxo-densidade')
    cluster(D_ST, F_ST, D_SL, F_SL, D_DA, F_DA, save, cluster_filename)
