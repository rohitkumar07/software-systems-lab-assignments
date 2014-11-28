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


# exception list
notcharlist = ['VOICES', 'SOMEBODY!', 'TRANSLATING', 'SURROUNDINGS:', 'ALL', 'CONTINUED:', 'AND', 'CONTINUED', 'AT', 'IT!', 'FL', 'MAN', 'MO-MEE-MO-MEE-MO!!!', 'SUSPICIONS:', 'JESUS!', 'FREEZE!', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(100) :
	notcharlist.append(str(i))

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
		charcount.append((distchar[index], 0))
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
				charcount[index] = (charcount[index][0], charcount[index][1] + 1)
				if temp < len(spl) - 1 :
					t = (charcount[index][0]).split()
					if spl[temp + 1] in distchar and t[len(t) - 1] != spl[temp + 1]:
						charcount[index] = (charcount[index][0] +" " + spl[temp + 1], charcount[index][1])
					# append the title of the name with character
			temp = temp + 1
		index = index + 1


print ("CHARACTER \t\t" + " REFERENCE COUNT \n")

for i in range(len(charcount)) :
	if charcount[i][1] != 0 :
		if len(charcount[i][0]) < 8 :
			print (charcount[i][0] + "\t\t\t\t" + str(charcount[i][1]))
		elif len(charcount[i][0]) < 16 :
			print (charcount[i][0] + "\t\t\t" + str(charcount[i][1]))
		else : 
			print (charcount[i][0] + "\t\t" + str(charcount[i][1]))

