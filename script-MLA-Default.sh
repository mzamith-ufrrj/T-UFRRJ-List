#!/usr/bin/bash
x=1
VAR=""
CONFIG="MLA-Default.xml"
INCLUSTER="cluster.adjusted.MLA-STANDARD-HR-1.5-0.*"
INFIXED="statistic.fixed.MLA-STANDARD-HR-1.5-0.*"
INPHOTO="statistic.photo.MLA-STANDARD-HR-1.5-0.*"
OUTCLUSTER="CA.MLA-STANDARD-HR-1.5-0.csv"
OUTFIXED="SF.MLA-STANDARD-HR-1.5-0.csv"
OUTPHOTO="SP.MLA-STANDARD-HR-1.5-0.csv"
while [ $x -le 95 ]
do
  VAR+="${x} "
  x=$(( $x + 1 ))
done
parallel ./exec-CA-lib-v2.0.py ::: $CONFIG ::: $VAR
cat $INCLUSTER > $OUTCLUSTER
cat $INFIXED > $OUTFIXED
cat $INPHOTO > $OUTPHOTO
rm -rf $INCLUSTER $INFIXED $INPHOTO
echo 'End the game!'