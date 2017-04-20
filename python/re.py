import re

def main():
	#email
	emails = "db@aol.com m@.com @apple.com db@.com"
	print(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", 
		emails))

if __name__ == '__main__':
	main()