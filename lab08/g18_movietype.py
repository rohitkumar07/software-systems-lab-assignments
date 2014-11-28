import operator

print("Enter the name of the file for which you want the details of script (eg - despicable.txt)");

while True:
	try:
		inputfile = input();
		moviefile = open(inputfile,'r');
		break
	except FileNotFoundError :
		print ("This file is not present in the directory. Please try again")

a = ["Mr.","Mrs."]

count = [0,0,0,0,0,0] #action, comedy, crime, mystery,romance,horror

genre = []
genre.append([" war","fight","struggle","attack","kill","conflict","rival","clash","quarrel","riot","dispute","operation","battle","hunt","revenge","violence","conflict","breach","hunt","run","dispute" ,"fear" ,"gun", "weapon"])

genre.append(["laugh","fun","comic","chuckle","giggle","gag","pun","mock","spoof","cheer","nonsense","smile","smirk","prank","amusing","enjoy","gossip","joke","fool","tease","amuse","hoopla","charm","celebrate","party","happy","kidding","mimic","witty"])

genre.append(["murder","drugs","prison","shot","dead",'gang','scandal','corruption','felony','breach','outrage','legal','conduct','prison','police','court','justice','weapon','gun','law'])

genre.append(["spy","detective","undercover","dispute","confusion","bluff","riddle","loot","risk","oracle","hunt","search","operation","secret","agent","informer","investigator","rival","invade","trait shot","murder","tension","shock","fear"])

genre.append(["love","romance","kiss","flower","sky","faith","believe","smile","cry","emotion","seduce","sex","faith","believe","smile","cry","emotion","lust","heart","eyes",
"beauty","trust","jealous","crush","wife"])

genre.append(["terror","panic","hatred","fear","dead","evil","curse","strain","stress","tension","scare","wick","brutality","creepy","insane","ugly","psycho","shock","dark","revenge","pain","illwill","venom","enmity","prejudice","monster","freak","beast","brute","savage","demon","torment","torture"])


for line in moviefile:
	splited = line.split();
	for i in range(len(splited)):
		splited[i] = splited[i].lower()
	for i in range(6):
		for to_find in genre[i]:
			for word in splited:
				if(to_find in word):
				#	print(to_find,',');	
					count[i] = count[i]+1;

genre = []

for i in range(len(count)) :
	genre.append((count[i], i))

genre.sort(key=operator.itemgetter(0))
genre.reverse()

first = genre[0][1]
second = genre[1][1]

genrelist = ['Action', 'Comedy', 'Crime/Drama', 'Mystery','Romance','Horror']

print ("The genre of this movie are: " + genrelist[first] + " & " + genrelist[second])







