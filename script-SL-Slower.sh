#!/usr/bin/bash
DIR=$(date +%Y%m%d-%H%M%S)
DIR="test.$DIR"
echo "Creating directory: $DIR"
if [ ! -d "$DIR" ]; then
  mkdir $DIR
fi
x=1
VAR=""
CONFIG="SL-Slower.json"
INCLUSTER="cluster.adjusted.SL-SLOW-HR-1.5-0.*"
INFIXED="statistic.fixed.SL-SLOW-HR-1.5-0.*"
INPHOTO="statistic.photo.SL-SLOW-HR-1.5-0.*"
OUTCLUSTER="CA.SL-SLOW-HR-1.5-0.csv"
OUTFIXED="SF.SL-SLOW-HR-1.5-0.csv"
OUTPHOTO="SP.SL-SLOW-HR-1.5-0.csv"
while [ $x -le 95 ]
do
  VAR+="${x} "
  x=$(( $x + 1 ))
done
parallel ./TModelCA++.exec ::: $CONFIG ::: $VAR
cat $INCLUSTER > $OUTCLUSTER
cat $INFIXED > $OUTFIXED
cat $INPHOTO > $OUTPHOTO
mv  $INCLUSTER $DIR
mv  $INFIXED  $DIR
mv  $INPHOTO $DIR
echo 'End the game!'
