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
	else:
		pass

if __name__ == "__main__":
	ap = argparse.ArgumentParser()
	ap.add_argument("-l","--list",required=True,metavar="",help="Subdomain List")
	ap.add_argument("-t","--thread",metavar="",default=5,type=int,help="thread number")
	args = ap.parse_args()

	main()
