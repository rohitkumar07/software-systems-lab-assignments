
------------------------------------------------------------------------------------
Assignment 8 - Python Programming
------------------------------------------------------------------------------------ 

Group No-18

1.Rohit Kumar 120050028
2.Suman Sourabh 120050031
3.Nitin Chandrol 120050035
------------------------------------------------------------------------------------

The scripts that we used for testing our python scripts are present in the same folder.

Algorithms that we have used for various implementations:

1. scriptinfo :- The program asks for an input-file and if a wrong file is given as input
		 then, it gives an error message and asks to re-enter the file using try command.
		 Picks up first line(non-empty) as the title and similarly for authors.
		 Separates the different authors using delimitors such as '&' and ','.

2. moviechar :- Through one iteration of the movie-script file, picks the characters by looking them 
		after Mr. or Mrs. and along with this picks the characters when they appear as 
		narrators and these extracted texts are then filtered by string operations like
		punctuation removal, every-word is converted to capitals so that every character occurs 
		only once in the list of distinct characters.
			Further through another parse, if a character in the list obtained as above is observed 
		and the next word is also in the above list, then they are clubbed together to form a single 
		character with the final count as the count of the first word.

3. movieactor:- For identifying the gender of a character:
		For every character we associated a list of male and female according to occurrence of following cases.

		    1-- If a line contains the character’s name and the same line(before “.”) contains a his/her 
			the character is male/	female is appended to the list associated to the character.

		    2--If a line contains the character’s name and the first word after “.” is He/She then 
			the male/female is appended to the list associated to the character.

		Then after we get the whole list associated to every character, observed which of “male” or “female” appears maximum time in 			the list of a character, which will be finally predicted to be the gender of character.
		For the main hero, we have used the maximum frequent occuring male in the script and similarly for the heroine.
		We assumed that the main story revolves around main character and villian, so the character appearing just less frequent than
		the most occuring character (hero or heroine) is tagged as villian.
		

4. movietype:-  For this part, we created a database specific to each genre with relevant and mostly used words in 
	        that genre movies. This database stored the minimal
	        eg - Horror genre words (terror panic hatred fear dead evil curse monster freak …...)
		Then we processed whole script to count the occurrence of  each genre words in it. Then 1st 2 maximum 
		count genre are returned as the movie tag.


------------------------------------------------------------------------------------

We have taken care of all plagiarism policies and whole assignment is our work.
For learning and implementing different python commands we have referred these sites-

1. Python 3 official documentation :- http://docs.python.org/3/tutorial/
2. Book :- Learn Python The Hard Way, 3rd Edition
3. Thinking Like a Computer Scientist :- http://www.openbookproject.net/thinkcs/python/english3e/
4. Last but not the least, Google!
