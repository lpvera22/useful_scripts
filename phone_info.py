# -*- coding: UTF-8
 
import requests
import sys
 
# Información
 
api_key = '23e1395c903b1ffa6292125af3c216a1'

 
# Petición
def petition(api_key,number):
 
	data = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (api_key, number))
	
	for key, value in data.json().items():
	 
	    print("%s: %s" % (key, value))


	
petition(api_key,sys.argv[1])
	



