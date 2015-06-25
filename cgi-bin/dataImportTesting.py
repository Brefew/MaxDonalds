#!/usr/bin/env python

import json
import urllib2
from pprint import pprint



print "Content-type: text/html"
print

print '''

<html>
	<head>
		<title>HW4 Carnes</title>
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

print stats[1]['Name'];


#with open('MaxDonalds.json') as stats:
#    data = json.loads(stats)
		
#pprint(data)
		
				
print '''
	
    <script type="text/javascript" src="//code.jquery.com/jquery-1.11.0.min.js"></script>

        <script>

        $( document ).ready(function() {
        '''
		
        
'''	
	</script>

'''


