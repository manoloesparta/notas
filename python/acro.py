string = input("String: ")

string = string.split(' ')

i = 0
a = ""
while i < len(string):
	a += string[i][0]
	i += 1

a = a.upper()
print(a)