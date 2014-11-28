#!/bin/bash

# Colonel Fitzwilliam got the new name Suman Sourabh
# Lady Catherine got the new name Nitin Chandrol
# Darcy got the new name Rohit Kumar

cat ./data/pnp_austen.txt | sed s/\'\'/\"/g | sed s/\`\`/\"/g | sed 's/\<Colonel Fitzwilliam\>/Suman Sourabh/g' |  sed 's/\<Lady Catherine\>/Nitin Chandrol/g' |  sed 's/\<Darcy\>/Rohit Kumar/g' > ./data/pnp_austen_cs296.txt
