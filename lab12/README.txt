
------------------------------------------------------------------------------------
Assignment 12 - MULTICLIENT GUI BASED PEER-TO-PEER CHAT IN JAVA (Using Java Swing and Thread)
------------------------------------------------------------------------------------ 

Group No-18

1. Rohit Kumar 120050028
2. Suman Sourabh 120050031
3. Nitin Chandrol 120050035
------------------------------------------------------------------------------------

Note :- make compile builds a jar executable in the the project root folder itself. 
	For executing it as a server execute the command "java -jar jtalkG18.jar server" and 
	for as a client "java -jar jtalkG18.jar client".


------------------------------------------------------------------------------------
Brief description of classes and the relation between them:

1. JMessage :- Stores the messages communicated through chat.

2. JPacket :- Inherited from JMessage and additionally, it stores the date and time when
		the message was communicated.

3. JChatSession :- Stores the messages communicated between the client and server and 
		   contains a method to print it. This class is the superclass of JChatComm.
		   Also finally it prints out the file with the log.

4. JChatComm :- Inherited from JChatSession. Has the main functionality to send and 
		receive JPackets via socket. 

5. JClient :- Inherited from Thread. Implements the client i.e. connects to the server 
	      via the protocol given and uses methods of JChatComm to enable conversation.

6. JServer :- Inherited from Thread. Implements the server i.e. waits for a client to 
	      connect and listens to it.

7. activeServerList :- It has a static list containing the name of currently connected
					sockets.

	----------------------------------------------------------
			INHERITANCE DIAGRAMS
	----------------------------------------------------------
			INHERITANCE 1
			--------------------		
	     -    JChatSession  -		
			--------------------
				 -
				---
				 -
			--------------------		
	      -    JChatComm     -		
			--------------------
			

			INHERITANCE 2
			-------------------
				Thread
			------------------
					-
				--------
					-
	     --------------------			
	     -      JClient     -			
	     --------------------	
		
				INHERITANCE 3
			-------------------
				Thread
			------------------
					-
				--------
					-
	     --------------------			
	     -      JServer     -			
	     --------------------			
			
		--------------------		
	    -      JMessage    -		
		--------------------
				 -
				 -
				 -
		--------------------		
	      -   JPacket     -		
			--------------------



------------------------------------------------------------------------------------

We have taken care of all plagiarism policies and the whole assignment is our work.
For learning JAVA Swing and implementing Java thread, we have referred these sources-

1. Java SE 6 Documentation
2. Java tutorials by Oracle	-	http://docs.oracle.com/javase/tutorial/


