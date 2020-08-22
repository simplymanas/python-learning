# browse laptop file in mob
# not other software required if you are in same network

#run this command in laptop (command prompt)
#python -m http.server

# bnrowse this in loca browser
# http://0.0.0.0:8000/

# ge the IP of the laptop

# in mobile browser
# http://<ip-of-laptop>>:8000

import socket


# Function to display hostname and
# IP address
def get_Host_name_IP():
	try:
		host_name = socket.gethostname()
		host_ip = socket.gethostbyname(host_name)
		print("Hostname :  ", host_name)
		print("IP : ", host_ip)
	except:
		print("Unable to get Hostname and IP")


get_Host_name_IP()