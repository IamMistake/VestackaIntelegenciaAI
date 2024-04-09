#!/bin/bash

Fruit=apple
Fruit[1]=orange
echo ${Fruit[*]}

case $1 in
  1) echo "eden" ;;
  2) echo "dva" ;;
  3) echo "tri" ;;
  *) echo "ne br" ;;
esac

#filetype=$(file "$2")
#
#case "$filetype" in
#  "$2: Zip archive"*) unzip "$2";;
#  "$2: gZip archive"*) gunzip "$2";;
#  "$2: gZip2 archive"*) bunzip2 "$2";;
#  *) echo "file $2 ne e zipped"
#    exit 1;;
#esac

count=$2

while [ $count -gt 0]
do
  echo $count
  count=$((count - 1))
  sleep 1
done
echo "BRAVOS"

