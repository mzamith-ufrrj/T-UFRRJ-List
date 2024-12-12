#!/opt/anaconda/bin/python
import matplotlib.pyplot as plt
import math
import numpy as np
import csv
import sys
def cluster(D, F, save, filename):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    ax.plot(D, F, color='blue',  linewidth=1)
    
    
    ax.set_xlabel('density')
    ax.set_ylabel('frenquency (%)')


    
    
    plt.xlim([0, 1])
    #plt.ylim([0, 3600])
    plt.xticks(np.arange(0, 1, 01.))
    #plt.yticks(np.arange(0, 3600, 500.0))
    plt.title('Velocities adjustment frequency')
    plt.grid(True)
    if save == 1:
        plt.savefig(filename, format='eps')
    else:
        plt.show()
    

def densidade_velocity(D, V, save, filename):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(D, V, marker='o', color='blue', alpha=1, s=1.5)
    
    ax.set_xlabel('density ')
    ax.set_ylabel('velocity [c/s]')

    ax.legend(['standard', 'slow', 'daring'])
    
    plt.xlim([0, 1])
    plt.ylim([0, 25])
    
    plt.xticks(np.arange(0, 1, 0.1))
    plt.yticks(np.arange(0, 25, 5))
    plt.title('Density-velocity')
    plt.grid(True)
    if save == 1:
        plt.savefig(filename, format='eps')
    else:
        plt.show()


def flow_velocity(F, V, save, filename):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(F, V, marker='o', color='blue', alpha=1, s=1.5)
    
    
    
    ax.set_xlabel('flow')
    ax.set_xlabel('velocity [c/s]')

    
    plt.xlim([0, 1.5])
    plt.ylim([0, 25])
    
    plt.xticks(np.arange(0, 1.5, 0.1))
    plt.yticks(np.arange(0, 25, 5))
    plt.title('Flow-velocity')
    plt.grid(True)
    if save == 1:
        plt.savefig(filename, format='eps')
    else:
        plt.show()


def flow_density(F, D, save, filename):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(D, F, marker='o', color='blue', alpha=1, s=1.5)
    
    
    ax.set_xlabel('density')
    ax.set_ylabel('flow')


    #ax.legend(['standard', 'slow', 'daring'])
    
    plt.xlim([0, 1])
    plt.ylim([0, 1.5])
    plt.xticks(np.arange(0, 1, 0.1))
    plt.yticks(np.arange(0, 1.5, 0.1))
    plt.title('Flow-density')
    plt.grid(True)
    if save == 1:
        plt.savefig(filename, format='eps')
    else:
        plt.show()
    

def loadData_cluster(filename, w):
    F = []
    D = []
    
    print('Reading file:', filename)
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            d = float(row[0]) * w
            f = float(row[3]) 
            D.append(d)
            F.append(f)

    return D, F

def loadData_statistic(filename, wf, wd, wv):
    F = []
    D = []
    V = []
    epsfilename =  filename.replace('.csv', '.eps')
    
    print('Reading file:', filename)
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
    
    save  = 1
    #pesos para colocar na mesma escala
#    weight_flow      = 3600 / 5
#    weight_density   = 133
#    weight_velocity  = 1.5 * 3.6
    weight_flow      = 1 / 5
    weight_density   = 1
    weight_velocity  = 1
    #arquivo de entrada gerado pelo simulador
            
    F, D, V = loadData_statistic(sys.argv[1], weight_flow, weight_density, weight_velocity)
    DC, FC  = loadData_cluster(sys.argv[2], weight_density)
            
    print('Grafico: fluxo-densidade')
    flow_density(F, D, save, 'flow-density.eps')
    flow_velocity(F, V, save, 'flow-velocity.eps')
    densidade_velocity(D, V, save, 'flow-velocity.eps')
    cluster(DC, FC, save, 'cluster.eps')
