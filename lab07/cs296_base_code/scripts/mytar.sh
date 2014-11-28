#!/bin/bash


if [[ $1 -eq 1 ]]
then
	tar -cf src.tar src 
	gzip src.tar
elif [[ $1 -eq 2 ]]
then
	for i in src/*
	do 
		gzip $i
	done
	tar -cf src.tar src

else echo "Invalid Argument"
fi
