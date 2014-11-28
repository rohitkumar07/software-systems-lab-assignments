package cs296MovieAnalysis;

import java.io.*;

public class FindGenre extends Movie{
	
	public FindGenre(String moviepath){
			super(moviepath);
		}
		
		
	/**
	 * Method to find genre of movie
	 * Here we used a database of most probable used words in a particular genre and 
	 * for each genre computed count and returned genre with best 2 counts
	 * @return
	 * @throws IOException
	 */
	 
	public void findGenre() throws IOException{
		String[] action = new String[] {"war","fight","struggle","attack","kill","conflict","rival","clash","quarrel","riot","dispute","operation","battle",
				"hunt","revenge","violence","conflict","breach","hunt","dispute" ,"fear" ,"gun", "weapon"};
		String[] comedy = new String[] {"laugh","fun","comic","chuckle","giggle","gag","pun","mock","spoof","cheer","nonsense","smile","smirk","prank","amusing",
				"enjoy","gossip","joke","fool","tease","amuse","hoopla","charm","celebrate","party","happy","kidding","mimic","witty"};
		String[] crime = new String[] {"murder","drugs","prison","shot","dead","gang","scandal","corruption","felony","breach","outrage","legal","conduct",
				"prison","police","court","justice","weapon","gun","law"};
		String[] mystery = new String[] {"spy","detective","undercover","murder","drugs","prison","bluff","riddle","loot","risk","oracle","hunt","search","operation",
				"secret","agent","informer","investigator","rival","invade","trait shot","murder","tension","shock","fear"};
		String[] romance = new String[] {"love","romance","kiss","flower","sky","faith","emotion","seduce","sex",
				"emotion","lust","heart","beauty","trust","jealous","crush","wife"};
		String[] horror = new String[] {"terror","panic","hatred","fear","dead","shot","curse","strain","stress","tension","scare","wick","brutality","creepy",
				"insane","ugly","shock","dark","revenge","pain","illwill","venom","enmity","prejudice","monster","freak","beast","brute","savage","demon","torment","torture"};
		
		int[] count =new int[] {0,0,0,0,0,0};
		
		String[] words = getMovieWords();
		
		
		for(int i=0;i<words.length;i++){
			for(int j=0;j<action.length;j++){
				//System.out.print("compare"+words[i].toLowerCase()+" "+action[j]);
				if(words[i].toLowerCase().matches(action[j])){
					//System.out.println(action[j]);
					count[0]++;
				}
			}
		}
		
		for(int i=0;i<words.length;i++){
			for(int j=0;j<comedy.length;j++){
				if(words[i].toLowerCase().matches(comedy[j]))
					count[1]++;
			}
		}
		for(int i=0;i<words.length;i++){
			for(int j=0;j<crime.length;j++){
				if(words[i].toLowerCase().matches(crime[j])){
					//System.out.println(crime[j]);
					count[2]++;
				}
			}
		}
		for(int i=0;i<words.length;i++){
			for(int j=0;j<mystery.length;j++){
				if(words[i].toLowerCase().matches(mystery[j]))
					count[3]++;
			}
		}
		for(int i=0;i<words.length;i++){
			for(int j=0;j<romance.length;j++){
				if(words[i].toLowerCase().matches(romance[j])){
					count[4]++;
					//System.out.println(romance[j]);
				}
			}
		}
		for(int i=0;i<words.length;i++){
			for(int j=0;j<horror.length;j++){
				if(words[i].toLowerCase().matches(horror[j])){
					count[5]++;
					//System.out.println(horror[j]);
				}
			}
		}
		int m1=0,m2=1;
		if(count[1] > count[0]){
			m2=0;
			m1=1;
		}
			
		for(int i=2;i<6;i++){
			//System.out.println("max is "+ m1 +" "+ m2);
			if(count[i] > count[m1]){
				m2=m1;
				m1=i;
			}
			else {
				if(count[i] > count[m2]){
					m2=i;
				}
			}
		}
		String[] genre= new String[] {"action","comedy","crime","mystery","romance","horror"};
		String[] ans= new String[2];
		ans[0]= genre[m1];
		ans[1]= genre[m2];
		System.out.println("The genre of this movie are " + ans[0] + " and "+ans[1] + ".");
	}
	
}
