#!/bin/bash
FOUND=`ps axu | grep "./mybins/cs296_18_exe" | grep -v "grep"| awk '{print $1}'`
if [[ "x"$FOUND"" != "x" ]]
then
#file = $(ps axu | grep "./mybins/cs296_18_exe" | grep -v "grep")
EXE_USR=`ps axu | grep "./mybins/cs296_18_exe" | grep -v "grep"| awk '{print $1}'`
P_ID=`ps axu | grep "./mybins/cs296_18_exe" | grep -v "grep"| awk '{print $2}'`
CURR_USR=`whoami`
echo "USER " "$EXE_USR"
echo "Process id " "$P_ID" 
	if [ "$EXE_USR" == "$CURR_USR" ]
	then
	echo "Do you want to quit ? (y/n) : "
	read data
		if [[ ( $data == y ) || ( $data == Y ) ]]
		then
		kill $P_ID
		else 
		echo "Process still running"
		fi
	else 
	echo "current user does not have permission to terminate the process"
	fi
else
echo "Basecode not running"
fi
