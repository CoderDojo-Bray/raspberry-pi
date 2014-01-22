<HTML>
<HEAD>
	<TITLE>Highscores Table</TITLE>
</HEAD>

<BODY>
<?
	//Write a title for our highscores table to the page. Echo writes the html in quotes to the browser
	echo "<b><center>High Scores Table</center></b><br><br>";

	// Connect to our coderdojo database - we only need to do this once for the page
	$user="root";
	$password="";
	$database="coderdojo";
	mysql_connect(localhost,$user,$password);
	@mysql_select_db($database) or die( "Unable to select database");

	
	
	// Assign a variable with our query to get all the records from the high score table
	$query="select * from highscore;";
	// Run the query
	$result=mysql_query($query);
	// Count the number of records we retrieved
	$num=mysql_numrows($result);	
	
	// Start a table to display our data
	echo "<table align='center'> <tr>   <th>Player</th>   <th>Game</th>   <th>Score</th>   <th>Time</th>  </tr>";
	
	//Loop through all the data we received and write each record out to the screen
	$i=0;
	while ($i < $num) {
		$playername=mysql_result($result,$i,"playername");
		$gamename=mysql_result($result,$i,"gamename");
		$score=mysql_result($result,$i,"score");
		$scoretime=mysql_result($result,$i,"scoretime");
		
		// Write the record
		echo "<tr> <td>$playername</td>  <td>$gamename</td>  <td>$score</td>  <td>$scoretime</td> </tr>";
		$i++;
	}
	
	// Finish our highscores table 
	echo "</table>";

	

	// 
	// Run more queries and show more tables here if we want them...
	//
	// $query="..........  and so on
	
	
	
	// close the connection to the database - we're done with the database now
	mysql_close();
	
	
?>

</BODY>
</HTML>
	