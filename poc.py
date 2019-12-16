import pydig

dns = pydig.query("www.guidebookdemo.com","A")

if dns:
	print("subdomain working")

else:
	print("subdomain fake")