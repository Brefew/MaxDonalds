<html>

    <head>

    <title>MaxDonald's</title>

    <script type="text/javascript" src="//code.jquery.com/jquery-1.11.0.min.js"></script>

	<script src="http://jquery-csv.googlecode.com/git/src/jquery.csv.js"></script>

    <script>

		$(document).ready(function() {
		});

	</script>

	<style>

	body {
		background-color: #DD1021;
	}

	</style>
    </head>
    <body>
	<center>

	<p>

	<font size = "10" face="verdana" color="yellow"><b>MaxDonald's<br>Get the Most out of Your Food!</b></font>

	</p>
<?php
$amount = $_POST['money']*100;



include("config.php");
$Price=0;
$checked = $_POST['options'];
for($i=0; $i < count($checked); $i++){
    echo "Selected " . $checked[$i] . "<br/>";
	
	
$qry = "SELECT sum(Price) FROM `data` where Type = '" . $checked[$i] . "'";
 $res = mysql_query($qry) or die(mysql_error());
 while($row = mysql_fetch_assoc($res)){
 
 $Price = $Price+$row['sum(Price)'];

 }
}

// echo $Price;
$temp= $amount-$Price;
echo "Your remaning amount in Cents:".$temp;

?>
<p id="msg">You may also buy</p>
<table border="1" align="center">
  <tr>
    <th scope="col">Product Name</th>
 <th scope="col">Price</th>
   
  </tr>
<?php


 $qry = "SELECT Type,Sum(Price) as total FROM `data` group by Type ";
 $res = mysql_query($qry) or die(mysql_error());
 while($row = mysql_fetch_assoc($res)){
echo "<tr>";
  echo "<td>&nbsp;" . $row['Type'] . "</td>";
    echo "<td>&nbsp;" . $row['total'] . "</td>";
 
  echo "</tr>";
 }
?>
</table>
<img src="Logo.png" height="200" width="250">

</center>

    </body>

</html>

