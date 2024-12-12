#! /home/mzamith/Apps/anaconda3/bin/python
import os
import sys
import csv
import matplotlib.pyplot as plt
import math
import numpy as np
from xml.dom import minidom
import cppyy
cppyy.include('Configure.hpp')
cppyy.include('CellularAutomata.hpp')
cppyy.load_library('libTModelCA++.so')
from cppyy.gbl import Configure, CellularAutomata
#------------------------------------------------------------------------------_
def cluster(D, F, save, filename):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(D, F, color='blue',  linewidth=1)


    ax.set_xlabel('density [v/km]')
    ax.set_ylabel('frenquency (%)')




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


def densidade_velocity(D, V, save, filename):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(D, V, marker='o', color='blue', alpha=1, s=1.5)

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


def flow_velocity(F, V, save, filename):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(F, V, marker='o', color='blue', alpha=1, s=1.5)



    ax.set_xlabel('flow [v/h]')
    ax.set_xlabel('velocity [km/h]')


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


def flow_density(F, D, save, filename):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(D, F, marker='o', color='blue', alpha=1, s=1.5)


    ax.set_xlabel('density [v/km]')
    ax.set_ylabel('flow [v/h]')


    #ax.legend(['standard', 'slow', 'daring'])

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
#-------------------------------------------------------------------------------
def build_graphics(configure, save, photo):


    #pesos para colocar na mesma escala
    weight_flow      = 3600 / 5
    weight_density   = 133
    weight_velocity  = 1.5 * 3.6
    #arquivo de entrada gerado pelo simulador
    #these files are also configured inside the C++ class
    statistic_photo_file  = "statistic.photo." + configure.mModelName + ".csv";
    statistic_fixed_file  = "statistic.fixed." + configure.mModelName + ".csv";
    cluster_adjusted_file = "cluster.adjusted." + configure.mModelName + ".csv";
    fd_file = 'flow-density. ' + configure.mModelName;
    fv_file = 'flow-velocity. ' + configure.mModelName;
    dv_file = 'density-velocity. ' + configure.mModelName;
    cluster_file = 'cluster.' + configure.mModelName + '.eps';
    if photo == 1:
        statistic_file = statistic_photo_file
        fd_file = fd_file + '.photo.eps'
        fv_file = fv_file + '.photo.eps'
        dv_file = dv_file + '.photo.eps'
    else:
        statistic_file = statistic_fixed_file
        fd_file = fd_file + '.fixed.eps'
        fv_file = fv_file + '.fixed.eps'
        dv_file = dv_file + '.fixed.eps'

    F, D, V = loadData_statistic(statistic_file, weight_flow, weight_density, weight_velocity)
    flow_density(F, D, save, fd_file)
    flow_velocity(F, V, save, fv_file)
    densidade_velocity(D, V, save, dv_file)

    DC, FC  = loadData_cluster(cluster_adjusted_file, weight_density)
    cluster(DC, FC, save, cluster_file)



#-------------------------------------------------------------------------------
def loadXML(xmlfilename):
    print('XML file: ', xmlfilename)
    xmlFile = open(xmlfilename ,'r')
    config = minidom.parse(xmlFile)
    xmlFile.close()


    global_param = config.getElementsByTagName('global-params')
    profiles = config.getElementsByTagName('profile')
    if len(global_param) > 1:
        print("Configure file with error")
        sys.exit(-1)



    configure = Configure()
    configure.setModelName(global_param[0].attributes['name'].value)

    #configure.mModelName = global_param[0].attributes['name'].value
    configure.mVMax = int(global_param[0].attributes['max-speed'].value)
    configure.mCellX =  int(global_param[0].attributes['cellX'].value)
    configure.mCellY = int(global_param[0].attributes['cellY'].value)
    configure.mDeltaH = float(global_param[0].attributes['size'].value)
    configure.mDefaultSize = float(global_param[0].attributes['default-size'].value)
    configure.mSTime = int(global_param[0].attributes['time-steps'].value)
    configure.mDTime = int(global_param[0].attributes['transiente-steps'].value)
    configure.mStTime = int(global_param[0].attributes['statistic-steps'].value)

    configure.mTypeModel = int(global_param[0].attributes['type-model'].value)

    configure.mFixed = int(global_param[0].attributes['photo'].value)
    configure.mPhoto = int(global_param[0].attributes['fixed'].value)
    configure.mLogCluster = int(global_param[0].attributes['logCluster'].value)
    configure.mLog = int(global_param[0].attributes['log'].value)

    configure.mDeceleration = int(global_param[0].attributes['deceleration'].value)
    configure.mTimePerception = float(global_param[0].attributes['time-perception'].value)
    configure.mRoadBlock =  int(global_param[0].attributes['road-block'].value)

    configure.mLogVehicles =  int(global_param[0].attributes['last-log-vehicles'].value)

    configure.setProfiles(len(profiles))

    index = 0
    acc = 0.0
    for prof in profiles:
        configure.setProfile(index, prof.attributes['name'].value,
                             float(prof.attributes['occ'].value),
                             int(prof.attributes['size'].value),
                             int(prof.attributes['max-speed'].value),
                             float(prof.attributes['betaA-acc'].value),
                             float(prof.attributes['betaB-acc'].value),
                             float(prof.attributes['inc'].value),
                             int(prof.attributes['desc'].value),
                             float(prof.attributes['left-p'].value),
                             float(prof.attributes['right-p'].value))

        index = index + 1
        acc = acc + float(prof.attributes['occ'].value)


    if acc > 1.0:
        print('ERROR: profiles occupation is greater than 1.0')
        sys.exit(-1)

    return configure

#-------------------------------------------------------------------------------
if __name__ == "__main__":
    #load config
    configfile = sys.argv[1]
    configure = loadXML(configfile)
    configure.print()
    save = 1
    #run simulation
    density = 0.01
    photo = 1

    while density <= 0.95:
       configure.mDensity = density
       CA = CellularAutomata()
       CA.init(configure)
       CA.exec()
       CA = 0
       density = density + 0.01
#build_graphics(configure, save, photo)
#build_graphics(configure, save, 0)
#plt diagrams
