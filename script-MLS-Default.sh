#!/usr/bin/bash
x=1
VAR=""
CONFIG="MLS-Default.xml"
INCLUSTER="cluster.adjusted.MLS-STANDARD-HR-1.5-0.*"
INFIXED="statistic.fixed.MLS-STANDARD-HR-1.5-0.*"
INPHOTO="statistic.photo.MLS-STANDARD-HR-1.5-0.*"
OUTCLUSTER="CA.MLS-STANDARD-HR-1.5-0.csv"
OUTFIXED="SF.MLS-STANDARD-HR-1.5-0.csv"
OUTPHOTO="SP.MLS-STANDARD-HR-1.5-0.csv"
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