
------------------------------------------------------------------------------------
Assignment 10 - JAVA PROGRAMMING
------------------------------------------------------------------------------------ 

Group No-18

1.Rohit Kumar 120050028
2.Suman Sourabh 120050031
3.Nitin Chandrol 120050035
------------------------------------------------------------------------------------

Note :- make compile builds the main class file. For executing it, please go to the bin directory formed 
	after compile target and execute this .class file [java MovieAnalysisG18] and it will do the execution.

------------------------------------------------------------------------------------

Use of OOP principles :


Interfaces:

Any class related to movie statistics should have the basic function like countScriptWord(to count the number of words in whole script, thus to determine the size of script), printCharCount(to print the list of all the characters with the number of occurrence of their names in the script of movie, to determine the significance )


The class MovieStatistics implements the interface MovieStateAbstract, so it necessarily implements all the functions defined in MovieStateAbstract(i.e., countScriptWords, printCharCounts and printCharCountsWithGender) and some other functions. 


------------------------------------
Polymorphism :

MovieAnalysisG18 is the class having the main function. It has a movie object. Also it has ms object of FindActor class. As the FindActor class is inherited from MovieStatistics. By polymorphism, it can also act as a object of MovieStatistics class. So to generate the output from MovieStatistics class and FindActor class, we used a unique object of FindActor class.

------------------------------------

Inheritance and other classes :- 

The MovieStatistics class is parent class for the FindActor class. In addition to the methods MovieStatistics gets from MovieStateAbstract, it has functions countMovieCharacters(returns a mapping of characters in the script of movie with the number of occurrence of their name), sortMovieCharacters(sorts the map returned from countMovieCharacters on the basis of the number of occurrences and returns it), determineCharGender(determine the gender of characters on the basis of the heuristics like appearance of his/her and he/she in the sentences and sortByComparator(sort the unordered mapping of character name with count of occurrence, on the basis of count of occurrence).

The class FindActor needs most of the functions defined in MovieStatistics, so to escape the pain of redefining things all over again the FindActor, we inherited it from the MovieStatistics so that the functions defined in MovieStatistics can be used directly. So it can be assumed by the inheritance that it has all the functions defined in MovieStatistics. Further was required to contain functions like findHero, findHeroine and findVillain. 

The Movie class has data type moviefilename and a constructor with parameter which takes moviepath.It has private methods like getMovieTitle and getMovieAuthor which returns appropriate string.It has public methods like printMovieTitle and printMovieAuthor to print appropriate information using get function.Method getMovieWords returns string array containing all words.Here we used BufferedReader and MovieAnalysisG18 class to process script file , here we read file line by line and using regex and spring.split stored all words in each line.

The FindGenre class has single method findGenre.Here we created a database storing most probable words in a particular genre and processed script file to find count for each genre type then genre with best 2 counts are printed.  



------------------------------------------------------------------------------------

We have taken care of all plagiarism policies and the whole assignment is our work.
For learning and implementing various OOP principles we have referred these sources-

1. Thinking in Java (Book)	-	http://www.mindviewinc.com/Books/TIJ/
2. Java SE 6 Documentation
3. Java tutorials by Oracle	-	http://docs.oracle.com/javase/tutorial/
4. Last but not the least, Google!


