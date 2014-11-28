package cs296MovieAnalysis;

import java.io.*;
import java.util.ArrayList;
/**
 * Public class Movie with single member variable Moviefilename
 *
 */
public class Movie {
	public String movieFilename;
	/**
	 * A Movie constructor with the parameter moviepath
	 * @param moviepath
	 */
	public Movie(String moviepath){
		movieFilename = moviepath;
	}
	/**
	 * This method returns moviename which is 1st non empty line of the script
	 * @return
	 * @throws IOException
	 */
	private String getMovieTitle() throws IOException{
		
		BufferedReader bf = new BufferedReader(new FileReader(movieFilename));
		String line = bf.readLine();
		while (line != null){
			line = line.replaceAll("[-+.^:',\"!?]","");
			if(line.length() > 1){
				return line.trim();
			}
			line = bf.readLine();
		}
		return null;
	}
	/**
	 * this method returns movieauthor which is 3rd non empty line of script
	 * @return
	 * @throws IOException
	 */
	private String getMovieAuthor() throws IOException{
		
		BufferedReader bf = new BufferedReader(new FileReader(movieFilename));
		String line = bf.readLine();
		int i=0;
		while (line != null){
			line = line.replaceAll("[-+.^:',!?]","");
			if(line.length() > 1){
				i++;
				if(i == 3)
					return line.trim();
			}
			line = bf.readLine();
		}
		return null;
	}
	/**
	 * this method calls movietitle method and prints it
	 * @throws IOException
	 */
	public void printMovieTitle() throws IOException{
		
		System.out.println("The title of the movie is : " + getMovieTitle());
	}
	/**
	 * this method calls movieauthor method and prints it
	 * @throws IOException
	 */

	public void printMovieAuthor() throws IOException{
		
		System.out.println("The author(s) of the movie is(are) : " + getMovieAuthor());
	}
	
	/**
	 * this method returns a string array with all words in the string
	 * @return
	 * @throws IOException
	 */
	public String[] getMovieWords() throws IOException{
		ArrayList<String> scripts = new ArrayList<String>();
		BufferedReader bf = new BufferedReader(new FileReader(movieFilename));
		String line = bf.readLine();
		String[] parts = new String[] { };
		while (line != null){
			line = line.replaceAll("[-+.^:',!?]","");
			if(line.length() > 1){
				line = line.trim();
				parts = line.split(" ");
				for(int i=0;i<parts.length;i++){
					if (parts[i].length() > 0)
					scripts.add(parts[i]);
				}
			}
			line = bf.readLine();
		}
		String[] ans = new String[scripts.size()];
		for(int j=0;j<scripts.size();j++){
			ans[j]=scripts.get(j);
			//System.out.println(ans[j]+" "+ans[j].length());
		}
		//System.out.println(scripts.size());
		return ans;
	}
	
	
}
