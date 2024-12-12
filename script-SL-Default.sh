#!/usr/bin/bash
DIR=$(date +%Y%m%d-%H%M%S)
if [ ! -d "$DIR" ]; then
  mkdir $DIR
fi
x=1
VAR=""
CONFIG="SL-Default.xml"
INCLUSTER="cluster.adjusted.SL-STANDARD-HR-1.5-0.*"
INFIXED="statistic.fixed.SL-STANDARD-HR-1.5-0.*"
INPHOTO="statistic.photo.SL-STANDARD-HR-1.5-0.*"
OUTCLUSTER="CA.SL-STANDARD-HR-1.5-0.csv"
OUTFIXED="SF.SL-STANDARD-HR-1.5-0.csv"
OUTPHOTO="SP.SL-STANDARD-HR-1.5-0.csv"
while [ $x -le 95 ]
do
  VAR+="${x} "
  x=$(( $x + 1 ))
done
parallel ./exec-CA-lib-v2.0.py ::: $CONFIG ::: $VAR
cat $INCLUSTER > $OUTCLUSTER
cat $INFIXED > $OUTFIXED
cat $INPHOTO > $OUTPHOTO
mv  $INCLUSTER $DIR
mv  $INFIXED  $DIR
mv  $INPHOTO $DIR
echo 'End the game!'