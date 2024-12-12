#!/usr/bin/bash
DIR=$(date +%Y%m%d-%H%M%S)
if [ ! -d "$DIR" ]; then
  mkdir $DIR
fi

