#!/bin/bash

RESULT=`up.py $1`

if [ $? -eq 0 ]
then
  echo $RESULT
  cd $RESULT
else
  exit 1
fi
