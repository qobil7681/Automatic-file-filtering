a = list()
b = list()
c = list()
symbols = ["'", ",", ".","ʻ", "/","*","‘","`","“",";",":","ʼ"," ","MFY","QFY","-","TATU","QMII","QDU","TIMI","(",")",'"']

z = False
while z == False:
    line = input()
    line=line.replace(" ", "")
    line = line.replace('x', 'h')
    if not line:
        z = True
    if line:
        for i in symbols:
            if i in line:
                line = line.replace(i, "")
        a.append(line)

k = False
while k == False:
    line = input()
    if not line:
        k = True
    if line:
        b.append(line)

t = False
while t == False:
    line = input()
    line = line.replace(" ", "")
    line = line.replace('x', 'h')
    if not line:
        t = True
    if line:
        for i in symbols:
            if i in line:
                line = line.replace(i, "")
        c.append(line)

my_dict = {}
result = {}

for i in range(len(a)):
    my_dict[a[i]] = int(b[i])


for i in c:
    if i in my_dict.keys():
        for j in my_dict.keys():
            if i == j:
                result[i] = my_dict[j]
    else:
        result[i] = "0"

for value  in result.values():
    print(value)
