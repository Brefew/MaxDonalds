#!/usr/bin/env python

## @package friesRun
# Explanation of this particular module
#
# Runs a test based on the fry category

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

## Byteify documentation
#
# Referenced from the HW4 function
# Converts the unicode of JSON keys
def byteify(input):
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

## response documentation
#
# Variable for holding the json input file
response = urllib2.urlopen("file:MaxDonalds.json")
## stats documentation
#
# A variable that acts as the converted json folder, having passed through byteify
stats = byteify(json.load(response))

## drink dictionary documentation
#
# Slice of the primary dictionary designated for drinks
drink = {}
## burger dictionary documentation
#
# Slice of the primary dictionary designated for burgers
burger = {}
## chicken dictionary documentation
#
# Slice of the primary dictionary designated for chicken
chicken = {}
## salad dictionary documentation
#
# Slice of the primary dictionary designated for salads
salad = {}
## dessert dictionary documentation
#
# Slice of the primary dictionary designated for dessert
dessert = {}
## fry dictionary documentation
#
# Slice of the primary dictionary designated for fries
fries = {}

## drCn Documentation
#
# The integer keeping track of the drink count index
drCn = 1
## buCn Documentation
#
# The integer keeping track of the burger count index
buCn = 1
## chCn Documentation
#
# The integer keeping track of the chicken count index
chCn = 1
## saCn Documentation
#
# The integer keeping track of the salad count index
saCn = 1
## deCn Documentation
#
# The integer keeping track of the dessert count index
deCn = 1
## frCn Documentation
#
# The integer keeping track of the fry count index
frCn = 1

#print stats[4];

## len documentation
#
# A value to keep track of the stats max length in a for loop that splits it up
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

<div id=moneyDiv style="display:none;">You must enter a valid amount from 0 to 50</div>

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

	<script>
	function myFunction(field) {
		//var burgerCheck = document.getElementById("Burger").checked;
		
		
		if(isNaN(field) || field <= 0 || field > 50) {
			document.getElementById('moneyDiv').style.display = "block";
			return(false);
		}
		
		
		else if(field == ""){
			//document.getElementById('moneyDiv').innerHTML = burgerCheck;
		}
		
		
	}
	</script>

	<button onclick="myFunction(document.getElementById('money').value)">Max your 'Donald's</button><br>
	
	

	<?xml version="1.0" encoding="UTF-8" standalone="no"?>
	<!-- Created with Inkscape (http://www.inkscape.org/) -->
	<svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" width="534.31348" height="505.01907" id="svg2" version="1.1" inkscape:version="0.48.4 r9939" sodipodi:docname="New document 1">
	  <defs id="defs4"/>
	  <sodipodi:namedview id="base" pagecolor="#ffffff" bordercolor="#666666" borderopacity="1.0" inkscape:pageopacity="0.0" inkscape:pageshadow="2" inkscape:zoom="1.4" inkscape:cx="375" inkscape:cy="291.42857" inkscape:document-units="px" inkscape:current-layer="layer1" showgrid="false" fit-margin-top="0" fit-margin-left="0" fit-margin-right="0" fit-margin-bottom="0" inkscape:window-width="1920" inkscape:window-height="1018" inkscape:window-x="-8" inkscape:window-y="-8" inkscape:window-maximized="1"/>
	  <metadata id="metadata7">
		<rdf:RDF>
		  <cc:Work rdf:about="">
			<dc:format>image/svg+xml</dc:format>
			<dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"/>
			<dc:title/>
		  </cc:Work>
		</rdf:RDF>
	  </metadata>
	  <g inkscape:label="Layer 1" inkscape:groupmode="layer" id="layer1" transform="translate(-1.7505249e-6,-547.34312)">
		<g id="g3038" transform="translate(-108.11493,259.63781)">
		  <path transform="matrix(1.0171988,0,0,1.0987766,-11.078088,-78.334082)" d="m 642.457,562.9433 c 0,126.9204 -117.58778,229.80971 -262.63965,229.80971 -145.05187,0 -262.63965,-102.88931 -262.63965,-229.80971 0,-126.9204 117.58778,-229.80971 262.63965,-229.80971 145.05187,0 262.63965,102.88931 262.63965,229.80971 z" sodipodi:ry="229.80971" sodipodi:rx="262.63965" sodipodi:cy="562.9433" sodipodi:cx="379.81735" id="path3018" style="fill:#DD1021;fill-opacity:1;stroke:none" sodipodi:type="arc"/>
		  <path id="path3008" d="m 448.94411,414.82163 c 28.14085,0 50.95599,115.00515 50.95599,256.87243 h 40.77494 c 0,-152.78374 -41.07523,-276.635 -91.73093,-276.635 -28.82345,0 -54.53662,37.22213 -71.35191,95.4273 -16.80804,-58.20517 -42.53087,-95.4273 -71.3507,-95.4273 -50.6557,0 -91.73575,123.85126 -91.73575,276.635 h 40.77975 c 0,-141.86728 22.81877,-256.87243 50.956,-256.87243 28.14568,0 50.97048,106.15905 50.97048,237.12155 h 40.76528 c 9.9e-4,-130.9625 22.81876,-237.12155 50.96685,-237.12155" inkscape:connector-curvature="0" style="fill:#ffcc00"/>
		</g>
	  </g>
	</svg>
	
	<!-- SVG taken from: http://logos.wikia.com/wiki/File:McDonald%27s_Philippines_logo_2011.svg -->

	</center>
    </body>
</html>
	
'''
#print document.getElementById("money").value;

## usr_money documentation
#
# A test value to apply to the code (displayed in cents)
usr_money = 529
## budget documentation
#
# Maintains the usr_money value
budget = usr_money
## minmoney documentation
#
# Maintains the budget value
minmoney = budget
## price documentation
#
# Standin price variable for the upcoming calculations
price = 0
## calpercent documentation
#
# Int for keeping track of the calories of food items per one cent
calpercent = 0
## run1 documentation
#
# Acts as a toggle to keep track of the upcoming while loop
run1 = 0
## item documentation
#
# An empty variable that takes the name of an item assigned later
item = ""
## order documentation
#
# Empty list to be filled with items that pass the tests for the items with the optimal calorie-per-cent rate
order = []
## work_dict documentation
#
# An empty dictionary that will handle the order[] list to be filled
work_dict = {}
for key in fries:
    if (fries[key]["Price"] * 100) <= budget:
        work_dict[fries[key]["Name"]] = (fries[key]["Calories"] / (fries[key]["Price"] * 100)), (fries[key]["Price"] * 100)
    print
#print work_dict
while (budget >= minmoney):
    if work_dict == {}:
        break
    calpercent = 0
    minmoney = budget 
    if run1 == 1:
        del work_dict[item]
        order.append(item)
       
    for key in work_dict:
        if work_dict[key][1] <= minmoney:
            minmoney = work_dict[key][1]
        if work_dict[key][0] > calpercent:
            calpercent = work_dict[key][0]
            item = key
            price = work_dict[key][1]
    budget -= price
    run1 = 1
#print order
if budget >= 0:
    order.append(item)
else:
    budget += price
print "Your order will be: "
for item in order: 
    print item, ","
print "and total to: $", (usr_money - budget)/100, "."
print "You will have $", (budget)/100, "remaining."
