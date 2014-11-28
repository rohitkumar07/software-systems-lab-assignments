import operator

print("Enter the name of the file for which you want the details of script (eg - despicable.txt)")

while True:
	try:
		inputfile = input()
		moviefile = open(inputfile,'r')
		break
	except FileNotFoundError :
		print ("This file is not present in the directory. Please try again")

charlist = []
# in this all characters(movie-characters) will be present in uppercase

notcharlist = ['VOICES', 'SOMEBODY!', 'GIRL', 'TRANSLATING', 'SURROUNDINGS:', 'ALL', 'CONTINUED:', 'AND', 'CONTINUED', 'AT', 'IT!', 'FL', 'MAN',
'MO-MEE-MO-MEE-MO!!!', 'SUSPICIONS:', 'JESUS!', 'FREEZE!', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(100) :
	notcharlist.append(str(i));

distchar = []
charcount = []

def club() :
	index = 0
	while index < len(charlist) :
		currentword = charlist[index]
		while currentword in charlist[index] :	# remove multiple occurences of the same character
			index = index + 1
			if index >= len(charlist) :
				break
		distchar.append(currentword)

def givecount() :
	index = 0
	while index < len(distchar) :
		charcount.append([distchar[index], 0])
		index = index + 1

	# pair of movie-character and its count

next_line_toPrint = False;

a = ["Mr.","Mrs."]

bad_punctuation = [")" , "(", ".", "-", "?", '!', "\""]

for line in moviefile :
	line = line.strip()
	splitlist = line.split()
	if len(splitlist) == 1 :
		if (splitlist[0]).isupper() :
			c = splitlist[0]
			if c[0] != "(" and not c[len(c) - 1] in bad_punctuation:
				charlist.append(c)
	if(next_line_toPrint):
		newline = splitlist[0]
		if newline[len(newline) - 1] in bad_punctuation :
			newline = newline[:(len(newline)-1)]
		charlist.append(newline.upper())
		next_line_toPrint = False;
	for title in a:
		indices = [i for i,val in enumerate(splitlist) if val==title]
		for index in indices:
			try:
				newline = splitlist[index+1]
				if newline[len(newline) - 1] in bad_punctuation :
					newline = newline[:(len(newline)-1)]
				charlist.append(newline.upper())
			except IndexError:
				next_line_toPrint = True


charlist = [char for char in charlist if not char in notcharlist]
# filter out unwanted words :-P

charlist.sort()

club()
givecount()

moviefile = open(inputfile,'r')

for l in moviefile :
	l = l.strip()
	spl = l.split()
	index = 0
	for i in distchar :
		temp = 0
		for j in spl :
			if i in j :
				charcount[index] = [charcount[index][0], charcount[index][1] + 1]
				if temp < len(spl) - 1 :
					t = (charcount[index][0]).split()
					if spl[temp + 1] in distchar and t[len(t) - 1] != spl[temp + 1]:
						charcount[index] = [charcount[index][0] +" " + spl[temp + 1], charcount[index][1]]
					# append the title of the name with character
			temp = temp + 1
		index = index + 1

hero = ['saves', 'watches', 'join']

moviefile = open(inputfile,'r')


gender = []

for i in range(len(distchar)):
	gender.append([distchar[i].lower(),[]])

for line in moviefile :
	line = line.strip()
	splited = line.split()
	for i in range(len(splited)):
		splited[i] = splited[i].lower()
	for j in range(len(gender)):
		if(gender[j][0] in splited):
			if(("His" in splited) or ("his" in splited)):
				gender[j][1].append("male");
			if(("Her" in splited) or ("her" in splited)):
				gender[j][1].append("female");
			
			for k in range(len(splited)):
				if("." in splited[k]):
					if k < len (splited) - 1 :
						if(("he" in splited[k+1]) or ("He" in splited[k+1])):
							gender[j][1].append("male");
#							print("male appended\n")
						elif(("he"in splited[k+1]) or ("He"in splited[k+1])):
							gender[j][1].append("female");
#							print("female appended\n")


def clubtog(l) :
	index = 0
	templist = []
	while index < len(l) :
		currentword = l[index]
		count = 0
		while currentword in l[index] :	# remove multiple occurences of the same character
			index = index + 1
			count = count + 1
			if index >= len(l) :
				break
		templist.append([currentword,count])
	return templist

for i in range(len(gender)):
	gender[i][1].sort()
	gender[i][1] = clubtog(gender[i][1])

for i in range(len(charcount)):
	(charcount[i]).append(gender[i][1])

charcount.sort(key=operator.itemgetter(1))

charcount.reverse()
			
def mostfreq(glist):
	if len(glist) == 2 :
		if glist[0][1] <= glist[1][1] :
			return "Male"
		else :
			return "Female"
	elif len(glist) == 0 :
			return "Undefined"
	else :
		if glist[0][0] == 'male' :
			return "Male"
		else :
			return "Female"


print ("CHARACTER \t\t" + " REFERENCE COUNT\t\t" + "Gender \n")

for i in range(len(charcount)) :
	if charcount[i][1] != 0 :
		if len(charcount[i][0]) < 8 :
			print (charcount[i][0] + "\t\t\t\t" + str(charcount[i][1]) + "\t\t\t" + mostfreq(charcount[i][2]))
		elif len(charcount[i][0]) < 16 :
			print (charcount[i][0] + "\t\t\t" + str(charcount[i][1]) + "\t\t\t" + mostfreq(charcount[i][2]))
		else : 
			print (charcount[i][0] + "\t\t" + str(charcount[i][1]) + "\t\t\t" + mostfreq(charcount[i][2]))

print ("The main hero of the movie is : " + charcount[0][0])

for i in range(len(charcount)) :
	if (mostfreq(charcount[i][2]) == "Female") :
		print ("The main heroine of the movie is : " + charcount[i][0])
		break

print ("The main villian of the movie is : " + charcount[2][0])



