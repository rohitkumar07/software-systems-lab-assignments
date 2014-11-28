package cs296MovieAnalysis;


import java.io.IOException;
import java.util.Map;

/**
 * Any class related to movie statistics should have the basic function like 
 * countScriptWord(to count the number of words in whole script, thus to determine the size of script), 
 * printCharCount(to print the list of all the characters with the number of occurrence of their names in 
 * the script of movie, to determine the significance )
 * 
 */

public interface MovieStatAbstract {

	int countScriptWords() throws IOException;
	
	public void printCharCounts() throws IOException;
	public void printCharCountsWithGender() throws IOException;	
}



