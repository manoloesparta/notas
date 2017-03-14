a = input("Mensaje: ")
b = ""
c = ""
for char in a:
	b = b + str(ord(char))
	if ord(char) < 91 and ord(char) > 64:
		c = c + str(ord(char)) + ","
	if ord(char) > 96 and ord(char) < 123:
		c = c + str(ord(char)) + ","
c = c[:-1]
print(b)

c = c.split(',')
print(c)

x = ""
i = 0
while True:
	x = x + str(chr(int(c[i-1])))
	i += 1
	if i > len(c):
		break
print(x[1:])

'''c = ""
for i in range(0, len(b)-1, 2):
	c = c + chr(int(b[i]+b[i+1]))
print(c)'''

# secret_string += str(ord(char) - 23)
# norm_string += chr(int(char_code) + 23)