# server_pull.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 11:53:41 2020

@author: iora
"""

import requests

def pull(user_group, secret_key, arm):
	url = ('http://172.27.118.20:5787/pull_arm/%s/%s/%s' % (user24,IyqHJZcK,str(arm)))
	
	while True:
		r = requests.get(url)
		if r.ok:
			output = r.json()['result']
			return(output)