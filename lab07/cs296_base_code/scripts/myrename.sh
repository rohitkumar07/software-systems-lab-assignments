#!/bin/bash

cd ./src

if [[ $1 -eq 1 ]]
then
	for i in *.cpp
	do
		mv $i $i.bak
	done

elif [[ $1 -eq 2 ]]
then
	ls | grep \.cpp | sed 'p;s/\.cpp/\.cpp.bak/' | xargs -n2 mv
else echo "Invalid command"
fi


