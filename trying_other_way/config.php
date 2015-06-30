<?php
$server = "localhost";
$user = "root";
$pass = "";
$dbname = "maxdonalds";

$conn = mysql_connect($server,$user,$pass);
if($conn){
 $seldb = mysql_select_db($dbname);
 if(!$seldb){
  die(mysql_error());
  
 }

}
else{
 die(mysql_error());
}
?>