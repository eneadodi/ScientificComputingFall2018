#!/usr/bin/env bash

file=fibs.csv

if [ -e fibs.csv.bk ]; then
  echo "fibs.csv already exists"
  echo "fibs.csv.bk already exists"
  echo "exiting code"
  exit
fi

if [ -e fibs.csv ]; then
  cp fibs.csv fibs.csv.bk
  rm fibs.csv
  echo "fibs.csv already exists"
  echo "creating backup"
fi

for i in $(seq 1000); do
  x=$(python fib.py $i)
  echo "$x" >> fibs.csv
done
