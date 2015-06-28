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
    <script>
		$(document).ready(function() {
            
		
		});
	</script>
    
	<style>
	body {
		background-color: #DD1021;
		
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
fish = {}
salad = {}
dessert = {}
fries = {}

drCn = 0
buCn = 0
chCn = 0
fiCn = 0
saCn = 0
deCn = 0
frCn = 0

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
	elif stats[i]["Type"] == "Fish":
		fish[fiCn] = stats[i]
		fiCn += 1
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
		var fish =
'''
print fish
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
        var count = 0;
		for (property in fries)
		{
		    if(fries.hasOwnProperty(property))
			{
				count++;
				//window.print(fries[property]);
			}
			//console.log(fries[property]);
		}
		//window.confirm(count - 1);
		
		var bT = document.getElementById("burgerTable");
		var row = bT.insertRow(0);
		var cell1 = row.insertCell(0);
		cell1.innerHTML = "New Cell1";
		
		
		
		
		
	});
	
	
	
	</script>

	</head>
    
        <body>
	<center>
	<p>
	<font size = "10" face="verdana" color="#FFCC00"><b>MaxDonald's<br>Get the Most out of Your Food!</b></font>
	</p>
	<input id='money' type='text' placeholder='How much will you spend?' name='money'><br>


	


	<p>
	<font color="white">What are you looking to eat?</font>
	</p>

	<table>
	  <tr>
	    <td>
	<input type="checkbox" name="Burger" id="Burger" value="burger">Burger
	    <div id="Burgerdiv" style="display:none">
                Here's all the burgers we have listed:
					<div style="display:table;">
						<table id="burgerTable" style="margin:5px;">
						</table>
					</div>
            </div>
            <script type="text/javascript">
                $('#Burger').change(function() {
                    $('#Burgerdiv').toggle();
                });
            </script>
            </td>
	    <td>
	<input type="checkbox" name="Chicken" id="Chicken" value="chicken">Chicken
            <div id="Chickendiv" style="display:none">
                Here's all the chicken items we have listed:
            </div>
            <script type="text/javascript">
                $('#Chicken').change(function() {
                    $('#Chickendiv').toggle();
                });
            </script>
            </td>
	    <td>
	<input type="checkbox" name="Fries" id="Fries" value="fries">Fries
            <div id="Friesdiv" style="display:none">
                Here's all the fries we have listed:
            </div>
            <script type="text/javascript">
                $('#Fries').change(function() {
                    $('#Friesdiv').toggle();
                });
            </script>
  
          </td>
	  </tr>
	  <tr>
	    <td>	
	<input type="checkbox" name="Drink" id="Drink" value="drink">Drink
            <div id="Drinkdiv" style="display:none">
                Here's all the drinks we have listed:
            </div>
            <script type="text/javascript">
                $('#Drink').change(function() {
                    $('#Drinkdiv').toggle();
                });
            </script>
    
            </td>
	    <td>
	<input type="checkbox" name="Salad" id="Salad" value="salad">Salad	
            <div id="Saladdiv" style="display:none">
                Here's all the salads we have listed:
            </div>
            <script type="text/javascript">
                $('#Salad').change(function() {
                    $('#Saladdiv').toggle();
                });
            </script>

            </td>
	    <td>
	<input type="checkbox" name="Dessert" id="Dessert" value="dessert">Dessert
            <div id="Dessertdiv" style="display:none">
                Here's all the desserts we have listed:
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


