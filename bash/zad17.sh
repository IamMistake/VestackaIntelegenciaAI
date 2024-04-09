#!/bin/bash

folder1=`ls -l $1 | grep '^-' | awk '{ print $9; }'`
br="0"

for file in $folder1
do
  if [ $file == '^[0-9][0-9]*[a-z]*\.out' ]
  then
    cp $file $2
  fi

  if [ -x $file ]
  then
    tmp=`wc -c $file`
    br=$(($br + $tmp))
  fi

done

echo $br