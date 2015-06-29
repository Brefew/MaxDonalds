#!/usr/bin/env python

import json
import urllib2
from pprint import pprint



print "Content-type: text/html"
print

print '''

<html>
    <head>
    <title>MaxDonald's</title>
    <script type="text/javascript" src="//code.jquery.com/jquery-1.11.0.min.js"></script>
	<script src="http://jquery-csv.googlecode.com/git/src/jquery.csv.js"></script>

    
	<style>
	body {
		background-color: #DD1021;
		font-size: 2em;	
	}
	
	th, td, tr {
		border: 1px solid black;
		border-collapse: collapse;
		font-size: 1em;
		padding-right: 10px;
		padding-left: 1px;
		padding-top: 1px;
		padding-bottom: 1px;
		white-space:nowrap;
		color: yellow;
	}

	
	#burgerData, #chickenData, #fryData, #drinkData, #saladData, #saladData, #dessertData {
			border: none;
			border-collapse: collapse;
			font-size: 100%;
			padding-right: 15;
			padding-left: 5;
			color: black;
		}
	
	
	
	#burgerTable, #chickenTable, #fryTable, #drinkTable, #saladTable, #dessertTable {
			border: 1px solid black;
			border-collapse: collapse;
		}
	
	</style>

        '''
	
#data = []
#data = json.loads(open('MaxDonalds.json').read())
#pprint(data)

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

response = urllib2.urlopen("file:MaxDonalds.json")
stats = byteify(json.load(response))

drink = {}
burger = {}
chicken = {}
salad = {}
dessert = {}
fries = {}

drCn = 1
buCn = 1
chCn = 1
saCn = 1
deCn = 1
frCn = 1

#print stats[4];

r = len(stats);

for i in range (0, r):
#	print stats[i]["Name"] + "<br>"
	if stats[i]["Type"] == "Drink":
		drink[drCn] = stats[i]
		drCn += 1
	elif stats[i]["Type"] == "Burger":
		burger[buCn] = stats[i]
		buCn += 1
	elif stats[i]["Type"] == "Chicken":
		chicken[chCn] = stats[i]
		chCn += 1
	elif stats[i]["Type"] == "Salad":
		salad[saCn] = stats[i]
		saCn += 1
	elif stats[i]["Type"] == "Dessert":
		dessert[deCn] = stats[i]
		deCn += 1
	elif stats[i]["Type"] == "Fries":
		fries[frCn] = stats[i]
		frCn += 1

#for i in burger:
#	print burger[i]["Price"]

#print burger
        
print '''	
     <script>

     $( document ).ready(function() {
		var drink =
'''
print drink
print '''
;
		var burger =
'''
print burger
print '''
;
		var chicken =
'''
print chicken
print '''
;
		var salad =
'''
print salad
print '''
;
		var dessert =
'''
print dessert
print '''
;
		var fries =
'''
print fries
print '''
;



		var drCn =
'''
print drCn
print '''
;
		var buCn =
'''
print buCn
print '''
;
		var chCn =
'''
print chCn
print '''
;
		var saCn =
'''
print saCn
print '''
;
		var deCn =
'''
print deCn
print '''
;
		var frCn =
'''
print frCn
print '''
;

		/*burger.sort(function(a, b){
			return a.id - b.id
		});*/

        var count = 0;
		for (property in fries)
		{
		    if(fries.hasOwnProperty(property))
			{
				count++;
				//console.log(fries[property]);
			}
			//document.write(JSON.stringify(fries[3]["Protein (g)"]));
			//document.write(buCn);
		}
		//window.confirm(count - 1);
		
		
		//var bD = document.getElementById("burger");
		
		var bT = document.getElementById("burgerTable");
		var cT = document.getElementById("chickenTable");
		var frT = document.getElementById("fryTable");
		var drT = document.getElementById("drinkTable");
		var sT = document.getElementById("saladTable");
		var deT = document.getElementById("dessertTable");
		
		/*function fillTable(targetDiv0, data0, index0,
								targetDiv, data, index) {
				for (var i = 1; i == index0; i++)
					{
						var row0 = targetDiv0.insertRow(i);
						var cell0 = row0.insertCell(0);
						cell0.innerHTML = JSON.stringify(data0[i]["Name"]);
						var cell1 = row0.insertCell(1);
						cell1.innerHTML = data0[i]["Calories"];
						var cell2 = row0.insertCell(2);
						cell2.innerHTML = data0[i]["Total Fat (g)"];
						var cell3 = row0.insertCell(3);
						cell3.innerHTML = data0[i]["Carbohydrates (g)"];
						var cell4 = row0.insertCell(4);
						cell4.innerHTML = data0[i]["Protein (g)"];
						var cell5 = row0.insertCell(5);
						cell5.innerHTML = data0[i]["Sodium (mg)"];
						var cell6 = row0.insertCell(6);
						cell6.innerHTML = data0[i]["Price"];
					}
					
				for (var i = 1; i == index; i++)
					{
						var row = targetDiv.insertRow(i);
						var cell = row.insertCell(0);
						cell0.innerHTML = JSON.stringify(data[i]["Name"]);
						var cell1 = row.insertCell(1);
						cell1.innerHTML = data[i]["Calories"];
						var cell2 = row.insertCell(2);
						cell2.innerHTML = data[i]["Total Fat (g)"];
						var cell3 = row.insertCell(3);
						cell3.innerHTML = data[i]["Carbohydrates (g)"];
						var cell4 = row.insertCell(4);
						cell4.innerHTML = data[i]["Protein (g)"];
						var cell5 = row.insertCell(5);
						cell5.innerHTML = data[i]["Sodium (mg)"];
						var cell6 = row.insertCell(6);
						cell6.innerHTML = data[i]["Price"];
					}
					//var bRow = bT.insertRow(1);
					//var bCell = bRow.insertCell(0);
					//bCell.innerHTML = "stuff";
					
				}*/
				
			function otherTry(targetDiv, foodData, cap) {
					var i = 1;
						
					for(i = 1; i < cap; i++)
						{
						var row = targetDiv.insertRow(1);
						var cell0 = row.insertCell(0);
						cell0.innerHTML = foodData[cap-i]["Name"];
						var cell1 = row.insertCell(1);
						cell1.innerHTML = JSON.stringify(foodData[cap-i]["Calories"]);
						var cell2 = row.insertCell(2);
						cell2.innerHTML = JSON.stringify(foodData[cap-i]["Total Fat (g)"]);
						var cell3 = row.insertCell(3);
						cell3.innerHTML = JSON.stringify(foodData[cap-i]["Carbohydrates (g)"]);
						var cell4 = row.insertCell(4);
						cell4.innerHTML = JSON.stringify(foodData[cap-i]["Protein (g)"]);
						var cell5 = row.insertCell(5);
						cell5.innerHTML = JSON.stringify(foodData[cap-i]["Sodium (mg)"]);
						var cell6 = row.insertCell(6);
						cell6.innerHTML = JSON.stringify(foodData[cap-i]["Price"]);
						if (i == (cap-1)){
							break;
						}
						}
						
					//var bRow = bT.insertRow(1);
					//var bCell = bRow.insertCell(0);
					//bCell.innerHTML = "DO SOMETHING";
					
			}
			
			//var bRow = bT.insertRow(1);
			//var bCell = bRow.insertCell(0);
			//bCell.innerHTML = "stuff1";
			//document.write(JSON.stringify(burger));
			
			//var total = 11;
			//document.write(buCn);
			otherTry(bT, burger, buCn);
			otherTry(cT, chicken, chCn);
			otherTry(frT, fries, frCn);
			otherTry(drT, drink, drCn);
			otherTry(sT, salad, saCn);
			otherTry(deT, dessert, deCn);
			
		//var row = bT.insertRow(1);
		//var cell1 = row.insertCell(4);
		//cell1.innerHTML = "New Cell1";
		
		
		//fillTable(bT, burger, buCn);
		
		
		
		
	});
	
	
	
	</script>

	</head>
    
        <body>
	<center>
	<p id="Header">
	<font size = "10" face="verdana" color="#FFCC00"><b>MaxDonald's<br>Get the Most out of Your Food!</b></font>
	</p>
	<input id='money' type='text' placeholder='How much will you spend?' name='money'><br>


	


	<p>
	<font color="white">What are you looking to eat?</font>
	</p>

	<table id="stats">
	  <tr id="topRow">
	    <td id="burgerData">
	<input type="checkbox" name="Burger" id="Burger" value="burger">Burger
	    <div id="Burgerdiv" style="display:none">
                <i>Here's all the burgers we have listed:</i>
					<div style="display:table;">
						<table id="burgerTable" style="width:30%">
							<tr>
								<td class="block"><b>Name</b></td>
								<td><b>Calories</b></td>
								<td><b>Total Fat(g)</b></td>
								<td><b>Carbs(g)</b></td>
								<td><b>Protein(g)</b></td>
								<td><b>Sodium(mg)</b></td>
								<td><b>Price</b></td>
						</table>
					</div>
            </div>
            <script type="text/javascript">
                $('#Burger').change(function() {
                    $('#Burgerdiv').toggle();
                });
            </script>
            </td>
	    <td id="chickenData">
	<input type="checkbox" name="Chicken" id="Chicken" value="chicken">Chicken
            <div id="Chickendiv" style="display:none">
                Here's all the chicken items we have listed:
					<div style="display:table;">
						<table id="chickenTable" style="width:30%">
							<tr>
								<td><b>Name</b></td>
								<td><b>Calories</b></td>
								<td><b>Total Fat(g)</b></td>
								<td><b>Carbs(g)</b></td>
								<td><b>Protein(g)</b></td>
								<td><b>Sodium(mg)</b></td>
								<td><b>Price</b></td>
						</table>
					</div>
            </div>
            <script type="text/javascript">
                $('#Chicken').change(function() {
                    $('#Chickendiv').toggle();
                });
            </script>
            </td>
	    <td id="fryData">
	<input type="checkbox" name="Fries" id="Fries" value="fries">Fries
            <div id="Friesdiv" style="display:none">
                Here's all the fries we have listed:
					<div style="display:table;">
						<table id="fryTable" style="width:30%">
							<tr>
								<td><b>Name</b></td>
								<td><b>Calories</b></td>
								<td><b>Total Fat(g)</b></td>
								<td><b>Carbs(g)</b></td>
								<td><b>Protein(g)</b></td>
								<td><b>Sodium(mg)</b></td>
								<td><b>Price</b></td>
						</table>
					</div>
            </div>
            <script type="text/javascript">
                $('#Fries').change(function() {
                    $('#Friesdiv').toggle();
                });
            </script>
  
          </td>
	  </tr>
	  <tr id="secondRow">
	    <td id="drinkData">	
	<input type="checkbox" name="Drink" id="Drink" value="drink">Drink
            <div id="Drinkdiv" style="display:none">
                Here's all the drinks we have listed:
					<div style="display:table;">
						<table id="drinkTable" style="width:30%">
							<tr>
								<td><b>Name</b></td>
								<td><b>Calories</b></td>
								<td><b>Total Fat(g)</b></td>
								<td><b>Carbs(g)</b></td>
								<td><b>Protein(g)</b></td>
								<td><b>Sodium(mg)</b></td>
								<td><b>Price</b></td>
						</table>
					</div>
            </div>
            <script type="text/javascript">
                $('#Drink').change(function() {
                    $('#Drinkdiv').toggle();
                });
            </script>
    
            </td>
	    <td id="saladData">
	<input type="checkbox" name="Salad" id="Salad" value="salad">Salad	
            <div id="Saladdiv" style="display:none">
                Here's all the salads we have listed:
					<div style="display:table;">
						<table id="saladTable" style="width:30%">
							<tr>
								<td><b>Name</b></td>
								<td><b>Calories</b></td>
								<td><b>Total Fat(g)</b></td>
								<td><b>Carbs(g)</b></td>
								<td><b>Protein(g)</b></td>
								<td><b>Sodium(mg)</b></td>
								<td><b>Price</b></td>
						</table>
					</div>
            </div>
            <script type="text/javascript">
                $('#Salad').change(function() {
                    $('#Saladdiv').toggle();
                });
            </script>

            </td>
	    <td id="dessertData">
	<input type="checkbox" name="Dessert" id="Dessert" value="dessert">Dessert
            <div id="Dessertdiv" style="display:none">
                Here's all the desserts we have listed:
					<div style="display:table;">
						<table id="dessertTable" style="width:30%">
							<tr>
								<td><b>Name</b></td>
								<td><b>Calories</b></td>
								<td><b>Total Fat(g)</b></td>
								<td><b>Carbs(g)</b></td>
								<td><b>Protein(g)</b></td>
								<td><b>Sodium(mg)</b></td>
								<td><b>Price</b></td>
						</table>
					</div>
            </div>
            <script type="text/javascript">
                $('#Dessert').change(function() {
                    $('#Dessertdiv').toggle();
                });
            </script>
  
          </td>
	  </tr>
	</table>

	<p></p>
	<br>
	<button type="button">Max your 'Donald's</button><br><br>

	<img src="Logo.png" height="200" width="250">

	</center>
    </body>
</html>
	
'''


