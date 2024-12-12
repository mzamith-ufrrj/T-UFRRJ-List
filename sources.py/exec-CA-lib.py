#!/home/mzamith/Apps/anaconda3/bin/python
import os
import sys
from xml.dom import minidom
import cppyy
cppyy.include('Configure.hpp')
cppyy.include('CellularAutomata.hpp')
cppyy.load_library('libTModelCA++.so')
from cppyy.gbl import Configure, CellularAutomata
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
                             int(prof.attributes['aheadway'].value),
                             int(prof.attributes['safedist'].value),
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