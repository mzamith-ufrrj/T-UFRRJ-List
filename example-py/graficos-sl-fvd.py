#!/home/mzamith/Apps/anaconda3/bin/python
import matplotlib.pyplot as plt
import math
import numpy as np
import csv
import sys


def cluster(D, V, save, filename):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(D, F, color='blue',  linewidth=1)


    ax.set_xlabel('density [v/km]')
    ax.set_ylabel('frenquency (%)')


    #ax.legend(['standard', 'slow', 'daring'])

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



def densidade_velocity(D_ST, V_ST, D_SL, V_SL, D_DA, V_DA, save, filename):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(D_ST, V_ST, marker='o', color='blue', alpha=1, s=1.5)
    ax.scatter(D_SL, V_SL, marker='o', color='red', alpha=1, s=1.5)
    ax.scatter(D_DA, V_DA, marker='o', color='green', alpha=1, s=1.5)

    ax.set_xlabel('density [v/km]')
    ax.set_ylabel('velocity [km/h]')

    ax.legend(['standard', 'slow', 'daring'])

    plt.xlim([0, 140])
    plt.ylim([0, 135])

    plt.xticks(np.arange(0, 140, 10.0))
    plt.yticks(np.arange(0, 140, 10.0))
    plt.title('Density-velocity')
    plt.grid(True)
    if save == 1:
        plt.savefig(filename, format='eps')
    else:
        plt.show()


def flow_velocity(F_ST, V_ST, F_SL, V_SL, F_DA, V_DA, save, filename):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(F_ST, V_ST, marker='o', color='blue', alpha=1, s=1.5)
    ax.scatter(F_SL, V_SL, marker='o', color='red', alpha=1, s=1.5)
    ax.scatter(F_DA, V_DA, marker='o', color='green', alpha=1, s=1.5)

    ax.set_xlabel('flow [v/h]')
    ax.set_xlabel('velocity [km/h]')

    ax.legend(['standard', 'slow', 'daring'])

    plt.xlim([0, 3600])
    plt.ylim([0, 140])

    plt.xticks(np.arange(0, 3600, 500.0))
    plt.yticks(np.arange(0, 140, 10.0))
    plt.title('Flow-velocity')
    plt.grid(True)
    if save == 1:
        plt.savefig(filename, format='eps')
    else:
        plt.show()


def flow_density(F_ST, D_ST, F_SL, D_SL, F_DA, D_DA, save, filename):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(D_ST, F_ST, marker='o', color='blue', alpha=1, s=1.5)
    ax.scatter(D_SL, F_SL, marker='o', color='red', alpha=1, s=1.5)
    ax.scatter(D_DA, F_DA, marker='o', color='green', alpha=1, s=1.5)


    ax.set_xlabel('density [v/km]')
    ax.set_ylabel('flow [v/h]')


    ax.legend(['standard', 'slow', 'daring'])

    plt.xlim([0, 135])
    plt.ylim([0, 3600])
    plt.xticks(np.arange(0, 136, 10.0))
    plt.yticks(np.arange(0, 3600, 500.0))
    plt.title('Flow-density')
    plt.grid(True)
    if save == 1:
        plt.savefig(filename, format='eps')
    else:
        plt.show()



def loadData(filename, wf, wd, wv):
    F = []
    D = []
    V = []
    epsfilename =  filename.replace('.csv', '.eps')

    print('Lendo arquivo:', filename)
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            f = float(row[2]) * wf
            d = float(row[3])  * wd
            v = float(row[4]) * wv
            F.append(f)
            D.append(d)
            V.append(v)

    return F, D, V

if __name__ == "__main__":
    #fixed or photo
    photo = 1
    save  = 1

    #pesos para colocar na mesma escala
    weight_flow      = 3600 / 5
    weight_density   = 133
    weight_velocity  = 1.5 * 3.6

    #arquivo de entrada gerado pelo simulador
    if photo == 1:
        filename_ST = 'statistic.photo.SL-STANDARD-HR-1.5.csv'
        filename_SL = 'statistic.photo.SL-SLOW-HR-1.5.csv'
        filename_DA = 'statistic.photo.SL-DARING-HR-1.5.csv'

        flow_density_filename     = 'flow-density_photo.eps'
        flow_velocity_filename    = 'flow-velocity_photo.eps'
        density_velocity_filename = 'density_velocity_photo.eps'
    else:
        filename_ST = 'statistic.fixed.SL-STANDARD-HR-1.5.csv'
        filename_SL = 'statistic.fixed.SL-SLOW-HR-1.5.csv'
        filename_DA = 'statistic.fixed.SL-DARING-HR-1.5.csv'

        flow_density_filename     = 'flow-density_fixed.eps'
        flow_velocity_filename    = 'flow-velocity_fixed.eps'
        density_velocity_filename = 'density_velocity_fixex.eps'


    print('Graficos')
    F_ST, D_ST, V_ST = loadData(filename_ST, weight_flow, weight_density, weight_velocity)
    F_SL, D_SL, V_SL = loadData(filename_SL, weight_flow, weight_density, weight_velocity)
    F_DA, D_DA, V_DA = loadData(filename_DA, weight_flow, weight_density, weight_velocity)

    print('Grafico: fluxo-densidade')
    flow_density(F_ST, D_ST, F_SL, D_SL, F_DA, D_DA, save, flow_density_filename)
    flow_velocity(F_ST, V_ST, F_SL, V_SL, F_DA, V_DA, save, flow_velocity_filename)
    densidade_velocity(D_ST, V_ST, D_SL, V_SL, D_DA, V_DA, save, density_velocity_filename)
