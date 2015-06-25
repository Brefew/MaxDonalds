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
			
'''

#print "$.ajax({dataType: 'json', url: "+burger+",data: data, success: success});"
#print burger

		
print '''
		
	});
	
	
	</script>

	</head>
    
    <body>
	<center>
	<p>
	<font size = "10" face="verdana" color="yellow"><b>MaxDonald's<br>Get the Most out of Your Food!</b></font>
	</p>
	<input id='money' type='text' placeholder='How much will you spend?' name='money'><br>
	
	<br>

	<p>
	<font color="white">What are you looking to eat?</font>
	</p>

	<table>
	  <tr>
	    <td>
	<input type="checkbox" name="Burger" value="burger">Burger
	    </td>
	    <td>
	<input type="checkbox" name="Chicken" value="chicken">Chicken
	    </td>
	    <td>
	<input type="checkbox" name="Fries" value="fries">Fries
	    </td>
	  </tr>
	  <tr>
	    <td>	
	<input type="checkbox" name="Drink" value="drink">Drink
	    </td>
	    <td>
	<input type="checkbox" name="Salad" value="salad">Salad	
	    </td>
	    <td>
	<input type="checkbox" name="Dessert" value="dessert">Dessert
	    </td>
	  </tr>
	</table>

	<p></p>
	<br>
	<button type="button">Max your 'Donald's</button>

	</center>
    </body>
</html>
	
'''


