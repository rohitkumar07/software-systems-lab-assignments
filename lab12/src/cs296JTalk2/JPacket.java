
package cs296JTalk2;

import java.awt.print.Printable;
import java.io.IOException;
import java.io.Serializable;
import java.sql.Timestamp;
import java.util.Date;

public class JPacket extends JMessage implements Serializable{
	Date date ;
	
	public JPacket(String messageString) {
		super(messageString);
		date = new Date();
	}

}
