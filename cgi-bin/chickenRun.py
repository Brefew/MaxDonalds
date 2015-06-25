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
		<script src="//code.jquery.com/jquery-1.11.2.min.js"></script>
	</head>
</html>
<?xml version="1.0" encoding="UTF-8" standalone="no"?>

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
				
print '''
	
    <script type="text/javascript" src="//code.jquery.com/jquery-1.11.0.min.js"></script>

        <script>

        $( document ).ready(function() {
        '''
		
        
'''	
	</script>

'''


