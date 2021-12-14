name1=input("enter first name =  ")
name2=input("enter second name = ")
for ch in name1:
	if ch in name2:	
		name2=name2.replace(ch,"")
		name1=name1.replace(ch,"")

name3=name1+name2

for ch in name3:
	if ch==" ":
		name3=name3.replace(ch,"")
name3=list(name3)
print(name3)
lngth=len(name3)
flms=list("FLAMES")
cnt=0
while(len(flms)>1):

	for i in range(len(flms)):
		cnt+=1
		if i==len(flms):
			break
		if cnt==lngth:
			flms.pop(i)
			cnt=0
flames=["Friends","Lovers","Affection","Marriage","Enemies","Siblings"]
for name in flames:
	if name.startswith(flms[0]):
		print("Relation B/W them:",name)