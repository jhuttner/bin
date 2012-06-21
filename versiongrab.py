#!/usr/local/bin/python

# versiongrab.py -- fast, clean output of AppNexus API versions
# Written by Joseph Huttner - jhuttner@appnexus.com

import shlex
import subprocess
import sys

def get_version(base_url):
	curl_url = base_url + "/status"
	command = " ".join(["curl", curl_url])
	print "\n======================================"
	print "".join(["\n", "Status for " + base_url, "\n"])
	subprocess.call(shlex.split(command))

def main(argv):
	apis = [
		"http://api.adnxs.com",
		"http://api.displaywords.com",
		"http://api.sand-08.adnxs.net",
		"http://hb.sand-08.adnxs.net",
		"http://dw-api.stage.adnxs.net",
		"http://api.stage.adnxs.net",
	]
	for i in apis:
		get_version(i)
	print "\n======================================\n"
	
	
if __name__ == "__main__":
	main(sys.argv[1:])
