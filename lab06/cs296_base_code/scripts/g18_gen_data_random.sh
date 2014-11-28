#!/bin/bash

cd ./../data
iterVal=1

while [ "$iterVal" -le 1500 ]
do
	rerunVal=1
	while [ "$rerunVal" -le 15 ]
	do
		number=$[$RANDOM%150 + 1]
		sed -n "$[$[$iterVal*150 - 150] + $number] p" g18_lab05data_02.csv >> g18_lab05data_random.csv
		rerunVal=$[$rerunVal + 1]
	done
	iterVal=$[$iterVal + 1]
done
