#!/usr/bin/env python
import sys
import os
import time
import urllib2

def main(): 
	addresses_filepath = 'addresses.txt'
	results_filepath = 'results.csv'

	if not os.path.isfile(addresses_filepath):
		print('File path {} does not exist. '.format(addresses_filepath))
		sys.exit()

	with open(results_filepath, 'w') as results_handler:
		with open(addresses_filepath) as fp:
			for line in fp:
				line = line.strip()
				output = line + ',' + query_macvendors(line)
				results_handler.write('%s\n' % output)
				time.sleep(1)

def query_macvendors(address):
	url = 'https://api.macvendors.com/'+address

	req = urllib2.Request(url)

	try:

		resp = urllib2.urlopen(req)

	except urllib2.HTTPError as e:

		if e.code == 404:
			return 'Not Found'
		else:
			return 'Error'
	
	else:
		return resp.read()
		
if __name__ == '__main__':
	main()
