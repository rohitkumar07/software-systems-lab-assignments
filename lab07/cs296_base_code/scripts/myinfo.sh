#!/bin/bash
function DIG_2 {
	NEW=`printf "%02d" $1`
	echo $NEW
}
CURR_D=`date +%j`
CURR_H=`date +%H`
DAY_1=$(( $(( $(( 318 - $CURR_D )) + 365 )) % 365 ))
DAY_2=$(( $(( $(( 67 - $CURR_D )) + 365 )) % 365 ))
DAY_3=$(( $(( $(( 97 - $CURR_D )) + 365 )) % 365 ))

echo Today is `date +%A", "%d" "%B", "%Y"."`
# echo "There are "  X1"weeks Y1 days and Z1 hours left for the birthday of <groupmember 1's name>


echo There are `DIG_2 $(( $DAY_1 / 7 ))` weeks `DIG_2 $(( $DAY_1 % 7 ))` days and `DIG_2 $(( 24 - $CURR_H ))` hours left for the birthday of Rohit Kumar 
echo There are `DIG_2 $(( $DAY_2 / 7 ))` weeks `DIG_2 $(( $DAY_2 % 7 ))` days and `DIG_2 $(( 24 - $CURR_H ))` hours left for the birthday of Suman Sourabh 
echo There are `DIG_2 $(( $DAY_3 / 7 ))` weeks `DIG_2 $(( $DAY_3 % 7 ))` days and `DIG_2 $(( 24 - $CURR_H ))` hours left for the birthday of Nitin Chandrol


echo Thank you for asking, `whoami`

#echo Your system has been running for `\proc\` days, Y4:Z4 hours.

timeinfo=`uptime | rev | cut -d " " -f 9- |rev  | cut -d " " -f 4- | rev | sed 's/,/sruoh /' | rev`
echo Your system has been running for $timeinfo.


diskinfo=$(df | awk '{ print $1, $5, $6 }' | grep "/$")
echo The current disk on which your home folder is located is $(echo $diskinfo | awk '{print $1}') and is $(echo $diskinfo | awk '{print $2}') full

ubuntuname=`lsb_release -i | awk '{ print $3 }'`" "`lsb_release -c | awk '{ print $2 }'`
echo You are running $ubuntuname and version `lsb_release -r | awk '{ print $2 }'` with Kernel `uname -r`

used=$(free -t | awk 'FNR == 2 {print $3}')
total=$(free -t | awk 'FNR == 2 {print $2}')

echo Your machine has `free -g | awk 'FNR == 2 {print $2}'` GB RAM. Of which $(( $(( $used * 100 ))/ $total ))% is in use.

echo This script has `wc -w ./scripts/myinfo.sh | awk '{print $1}'` words, `wc -l ./scripts/myinfo.sh | awk '{print $1}'` lines and `wc -m ./scripts/myinfo.sh | awk '{print $1}'` characters "(without counting whitespace)"

