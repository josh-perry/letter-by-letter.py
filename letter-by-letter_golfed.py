r=raw_input
i=r()
o=r()
print i
for x in range(len(i)):
 if i[x]!=o[x]:i=i[:x]+o[x]+i[x+1:];print i