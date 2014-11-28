package cs296MovieAnalysis;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Map;
import java.util.Map.Entry;


/**
 * \brief Class to find the Hero and Heroine and Villain
 * 
 * @extends MovieStatics
 * 
 * Since the findHero and findHeroine function rely upon the various statistics of the movieStatistics class, inheriting this class from
 * movieStatistics will. Additionally it uses many functions
 *  of MovieStatics. 
 *
 */

public class FindActors extends MovieStatistics {
	
	
	/**
	 * @param movie Movie class passed to the constructor of this class
	 * 
	 * This is the constructor for this class which is again inherited from the superclass using the super method.
	 */
	 
	public FindActors(Movie movie) {
		super(movie);
	}
	
	/**
	 * \brief Prints the hero of script.
	 * 
	 * This function uses two variables, movieCharsCount and genderCount which are obtained from the method sortMovieCharacters() 
	 * and determineCharGender() respectively which are inherited from MovieStatics
	 * 
	 * The male whose name is most frequent in the script (i.e., the top most male character in the map movieCharsCount) is assigned 
	 * to be the hero.
	 * 
	 * @throws IOException 
	 * 
	 */
	
	public void findHero() throws IOException {
		
		Map<String, Integer> movieCharsCount =  sortMovieCharacters();
		ArrayList<Integer> genderCount = determineCharGender();
		
		String hero = "";
		int index = 0;
		for (Entry<String, Integer> entry : movieCharsCount.entrySet()) {
			if(genderCount.get(index) > 0) {
				hero = entry.getKey();
				break;
			}
			index++;
			
		    //System.out.println("Key = " + entry.getKey() + ", Value = " + entry.getValue());
		}		
		
		System.out.println("The hero of the movie is : "+hero);
		
	}
	
	/**
	 * Prints the heroine of script.
	 * This function again uses two variables, movieCharsCount and genderCount which are obtained from the method sortMovieCharacters() 
	 * and determineCharGender() respectively which are inherited from MovieStatics
	 * 
	 * The female whose name is most frequent in the script (i.e., the topmost female character in the map movieCharsCount) is 
	 * assigned to be the heroine.
	 * 
	 * @throws IOException 
	 * 
	 */
	
	public void findHeroine() throws IOException {
		Map<String, Integer> movieCharsCount =  sortMovieCharacters();
		ArrayList<Integer> genderCount = determineCharGender();
		
		String heroine = "";
		int index = 0;
		for (Entry<String, Integer> entry : movieCharsCount.entrySet()) {
			if(genderCount.get(index) < 0) {
				heroine = entry.getKey();
				break;
			}
			index++;
			
		    //System.out.println("Key = " + entry.getKey() + ", Value = " + entry.getValue());
		}			
		System.out.println("The heroine of the movie is : "+heroine);
		
	}
	
	/**
	 * Method returns the movie villain 
	 * Here we counted the occurrence of few probable characters in last part of the script 
	 * @return
	 * @throws IOException
	 */
	public void findVillain() throws IOException{
	
		Map<String, Integer> movieCharsCount =  sortMovieCharacters();
		ArrayList<Integer> genderCount = determineCharGender();
		int index = 0,temp = 0;
		
		for (Entry<String, Integer> entry : movieCharsCount.entrySet()) {
			if(genderCount.get(temp) > 0 && index == 1) {
				System.out.println("The villain of the movie is : "+ entry.getKey());
					break;
			}
			
			temp++;
			if(genderCount.get(index) > 0) {
				index++;
			}
		}
		
	}
}
