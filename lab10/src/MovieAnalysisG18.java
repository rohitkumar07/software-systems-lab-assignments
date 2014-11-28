import cs296MovieAnalysis.*;

import java.io.*;

public class MovieAnalysisG18 {
	
	/**
	 * \brief The main method
	 * 
	 * This is the main method which is executed first and outputs the name of the movie and authors, 
	 * the character count and gender table, the main hero, heroine, villain and the movie genre.
	 *
	 */
	public static void main(String[] args) throws IOException{
		
		InputStreamReader stream = new InputStreamReader(System.in);
		BufferedReader bf = new BufferedReader(stream);
		
		System.out.println("Please give the absolute path of the script file. eg:- /home/rohit/Desktop/g18_lab10/scripts/despicable.txt");
		
		String input = bf.readLine();
		
		Movie m = new Movie(input);
		m.printMovieTitle();
		m.printMovieAuthor();
		
		FindActors ms = new FindActors(m);
		FindGenre fj = new FindGenre(input);
		
		//ms.countMovieCharacters();
		ms.printCharCounts();
		ms.printCharCountsWithGender();
		ms.findHero();
		ms.findHeroine();
		ms.findVillain();
		fj.findGenre();
	}
}






