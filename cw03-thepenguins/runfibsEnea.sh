
#!/usr/bin/env bash

file=fibs.csv

if [ -e fibs.csv.bak ]; then
  echo "Both fibs.csv and fibs.csb.bak exist. Exiting code"
  exit
fi

if [ -e fibs.csv ]; 
then
  cp fibs.csv fibs.csv.bak
  rm fibs.csv
  echo "fibs.csv exists. Creating file fibs.csv.bak"
fi

  touch fibs.csv
  for i in $(seq 1000); do
  x=$(python fibEnea.py $i)
  echo "$x" >> fibs.csv
  done
