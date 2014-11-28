
history | sed 's/[ ]*[0-9]*[ ]*//' | cut -d " " -f 1 | sort | uniq -c | sort -nr | head -n 10 | awk '{print $1, $2}'
