#! /home/mzamith/Apps/anaconda3/bin/python
import timeit
from subprocess import PIPE, Popen, TimeoutExpired
import os
import cppyy
import sys
from xml.dom import minidom
cppyy.include('Configure.hpp')
#cppyy.add_include_path('/home/mzamith/Documents/Projetos/T-UFRRJ/Traffic-Model-CA++/release-05/cpp')
cppyy.load_library('libTModelCA++.so')
from cppyy.gbl import Configure

def XML2BIN(xmlfilename):
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
    configure.mModelName = global_param[0].attributes['name'].value
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
    configure.print()
    print('-----------------------------------------')
    #configure.saveConfigFile('Hello World!')
    binfilename = configure.mModelName + '.bin'
    configure.saveConfigFile(binfilename)

    if acc > 1.0:
        print('ERROR: profiles occupation is greater than 1.0')
        sys.exit(-1)

    return binfilename
# ==------------------------------------------------------------------------------------------------------------------
config = XML2BIN(sys.argv[1])
density = 0.01
while density <= 0.9:
    print('\n\t\t\033[1;31;48m *--> PID: ', os.getpid(), '\033[1;33;48m')

    cmd = './TModelCA++ {1} {0:.2f}'.format(density, config)
    os.system(cmd)
    density = density + 0.01
