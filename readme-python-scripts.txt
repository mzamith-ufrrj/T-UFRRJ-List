script python help file

betaPDF.py

exec-bin.py: runs simulation for all densities from binary config files
             Syntax: exec-bin.py <binary config file>

exec-v2.0.py

graficos.py: creates state and cluster graphics of one behavior which is an input parameter
             syntax graficos.py <csv log file>

graficos-sl-cluster.py: creates the influence cluster frequency. Syntax graficos-sl-cluster.py
                        In and out files are set inside script

graficos-sl-fvd.py: creates state diagrams (flow-density, velocity-density, flow-velocity and cluster frequency)
                    It requires 3 files, considering 3 drivers' behavior
                    Syntax: graficos-sl-fvd.py -> in and out files are set inside script

xml2bin.py : converts XML config file to binary one -> xml2bin.py <file.xml>
             It also creates binary file automatic based on name of simulation set inside XML config file
