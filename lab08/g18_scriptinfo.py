print("Enter the name of the file for which you want the details of script (eg - despicable.txt)")

while True:
	try:
		inputfile = input()
		break
	except FileNotFoundError :
		print ("This file is not present in the directory. Please try again")
	
moviefile = open(inputfile,'r')

while(1):
	a = moviefile.readline()
	if a != '\n' :
		while(a[0]==" "):
			a = a[1:]	# removing initial spaces present in the line
		print ("The title of the movie is: " + a)
		break

# omitting "Written By"
while(1):
        a = moviefile.readline()
        if a != '\n' :
               	break

authorlist = []

while(1):
	a = moviefile.readline()
	if a != '\n' :
		while(a[0]==" "):
			a = a[1:]
		# equivalently a = a.rstrip()
		i = 0
		while (1):
			temp = ""
			while a[i] != '&' or a[i] != ',':
				temp = temp + a[i]
				i = i + 1
				if i >= len(a):
					break
			authorlist.append(temp)
			# print (i) 
			if i >= len(a):
				break
			if a[i] == '&' or a[i] == ',':
				i = i + 1
		break

print("The author(s) of this movie script is(are) : ")

for i in range(len(authorlist)) :
	print ("Author " + str(i+1) + " : " + authorlist[i])

