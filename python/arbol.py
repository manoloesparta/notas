'''
h = input("Num: ")
h = int(h)

i = 0
b = "#\n"

while i < h:
	i += 1
	a = 0
	b = b + "#"
	while a < i:
		a += 1
		b = b + "##"
		if a == i:
			b = b + "\n"
b = b + "#"
print(b)

i = 0
a = 0
c = []

while i < len(b):
	i += 1
	a = b.find("\n",a+2)
	c.append(a)

i = 0
d = []

for i in c:
	if i not in d:
		d.append(i)

d.remove(-1)
primer = d[-1:]
d = primer + d
del d[-1]

print(d)

i = 0
a = 0
aa = 1
j = 0
espacio = ""
amen = 0
z = 0

for x in d:
	y = (d[aa] - d[a]) - 
	aa += 1
	a +=
	while j < y:
		j += 1
		espacio += " "
	b.find("#",d[amen]-1)
	amen += 1
	b = b[:z] + espacio + b[:-1]
	z += 1
	print(b)
'''

tree_height = input("How tall is the tree : ")
tree_height = int(tree_height)
spaces = tree_height - 1
hashes = 1
stump_spaces = tree_height - 1
while tree_height != 0:
 
    for i in range(spaces):
        print(' ', end="")

    for i in range(hashes):
        print('#', end="")

    print()
    spaces -= 1 
    hashes += 2 
    tree_height -= 1
 
for i in range(stump_spaces):
    print(' ', end="")
 
print("#")



