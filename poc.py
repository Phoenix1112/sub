import pydig
import tldextract
import argparse
from concurrent.futures import ThreadPoolExecutor

def main():
	with open(args.list,"r",encoding="utf-8") as f:
		for i in f.read().lower().split("\n"):
			if i:
				parse = tldextract.extract(i)
				
				if not len(parse.subdomain) > 63:
					with ThreadPoolExecutor(max_workers=args.thread) as executor:
						executor.submit(resolver,i)
				else:
					pass
			else:
				pass

def resolver(subdomain):
	dns = pydig.query(subdomain,"A")

	if dns:
		print(subdomain)
		
		if args.output:
			sendtowrite(subdomain)
		else:
			pass
	
	else:
		pass

def sendtowrite(subdomain):
	with open(args.output,"a+",encoding="utf-8") as o:
		o.write(str(subdomain)+"\n")

if __name__ == "__main__":
	ap = argparse.ArgumentParser()
	ap.add_argument("-l","--list",required=True,metavar="",help="Subdomain List")
	ap.add_argument("-o","--output",required=False,metavar="",help="output")
	ap.add_argument("-t","--thread",metavar="",default=5,type=int,help="thread number")
	args = ap.parse_args()

	main()