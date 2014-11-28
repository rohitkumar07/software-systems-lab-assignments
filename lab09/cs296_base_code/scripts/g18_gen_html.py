#! /usr/bin/env python3

texfile = open("./doc/g18_prof_report.tex")

htmlfile = open("./doc/g18_lab09_report.html", 'w')

htmlfile.write("<html>\n\t<body>\n")

htmlfile.write("<title>Lab Report of Timing Experiments</title>\n")

htmlfile.write("<style>\n")
htmlfile.write("\t .cent{text-align:center; margin-left:auto; margin-right:auto;}\n")
htmlfile.write("\t .eqn{text-align:center; font-size: 20px; margin-left:auto; margin-right:auto;}\n")
htmlfile.write("\t pre{text-align:left; font-size: 16px; padding:25px; background-color:#eee}\n")

htmlfile.write("\t p{text-align:left; margin-left:auto; margin-right:auto;font-size: 21px;}\n")
htmlfile.write("</style>\n")

start = '{Lab 5 Timing Experiments}'
while(1):
	line = texfile.readline()
	if start in line :
		break

htmlfile.write("<div class = \"cent\">\n")
htmlfile.write("<h1>")
htmlfile.write(start[1:len(start)-1])
htmlfile.write("</h1>\n")
htmlfile.write("</div><br>\n")

def colon(l):
	res = ""
	index = 0
	while index < len(l) :
		if l[index] == "{" :
			break
		index = index + 1
	if index == len(l) :
		return res
	index = index + 1	
	while index < len(l) :
		if l[index] == "}" :
			break
		res = res + l[index]
		index = index + 1
	return res

def purify(l) :
	a = l.split()
	for i in range(len(a)):
		if "{" in a[i] :
			a[i] = colon(a[i])
		for j in range(len(a[i])) :
			if a[i][j] == "}" :
				a[i] = a[i][0:j] + a[i][j+1:(len(a[i]) - 1)]		
	res = ""
	for i in range(len(a)):
		res = res + a[i] + " "
	if res != "" :
		if res[len(res) - 2] == "-" :
			res = res + "<br>"
	return res	

def putdelta(l):
	res = ""
	if "\\Delta" in l :
		res = res + " &Delta; "
		res = res + colon(l[6:])
		return res
	else :
		return l	

nextbegin = False

for line in texfile :
	line = line.strip()
	if len(line) == 0 :
		continue
	if line[0] == "%" :
		continue
	if line[0] in "\\" :
		line = line[1:]
		if "paragraph" in line:
			htmlfile.write("<p>")
			while(1) :
				line = texfile.readline()
				if "begin" in line or "section" in line :
					nextbegin = True
					break
				htmlfile.write(purify(line))
			htmlfile.write("</p>\n")
		if "Difference between time and gettimeofday" in line :
			break
		if "lstlisting" in line:
			htmlfile.write("<pre>\n")
			while(1) :
				line = texfile.readline()
				if "\end" in line :
					break
				s = list(line)
				for i in range(len(s)) :
					if s[i] == "<" :
						s[i] = "<code><</code>"
				line = "".join(s)
				htmlfile.write(line)
			htmlfile.write("</pre>\n")		

		if "equation" in line:
			line = texfile.readline()
			htmlfile.write("<div class = \"eqn\">\n")
			s = line.split()
			i = 0
			while i < len(s) :
				if s[i] == "\\Delta" :
					htmlfile.write(" &Delta; ")
				elif "rac" in s[i] :
					htmlfile.write("<i>(" + putdelta(colon(s[i+1])) + ")</i>/(" + putdelta(colon(s[i+2]))+ ")")
					i = i + 2
				else :
					htmlfile.write(putdelta(s[i]))
				i = i + 1
			htmlfile.write("</div>\n")
			line = texfile.readline()

		if "section" in line:
			htmlfile.write("<hr><div class = \"cent\">\n")
			htmlfile.write("<h2>")
			htmlfile.write(colon(line))
			htmlfile.write("</h2>\n")
			htmlfile.write("</div>\n")
		if "begin" in line:
			if "itemize" in line :
				htmlfile.write("<ul>\n")
				while(1) :
					line = texfile.readline()
					if "\end" in line :
						break
					if line[0] in "\\" :
						htmlfile.write("<li>\n")
						htmlfile.write("\t" + (purify(line[5:])))
						htmlfile.write("</li>\n")
					else :
						htmlfile.write(purify(line))
				htmlfile.write("</ul>\n")

			if "center" in line :
					htmlfile.write("<div class = \"cent\">\n")
					line = texfile.readline()
					htmlfile.write("<img src=" + "\""+"./../plots/g18_lab09_plot0")
					imagename=colon(line)
					htmlfile.write(imagename[len(imagename) - 1] + ".png\"" + " align=\"middle\"")
					htmlfile.write("height=\"450px\" width=\"600px\"> <br>\n")	
					line = texfile.readline()
					if not "center" in line :
						htmlfile.write(colon(line))
					htmlfile.write("</div>\n<br>\n")


htmlfile.write("\t\t<hr>\n")
htmlfile.write("\t</body>\n</html>\n")

