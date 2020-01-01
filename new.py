import numpy as np  
import csv, math

file = open("data.txt")
clean = list(file)
cl = [i.split(',') for i in clean]
out = np.concatenate(cl).tolist()
out.remove("")
#print(len(out))
n = 4
list_ = []
i=0
while(i<len(out)):
	x = out[i:i+n]
	#print(x)
	s = x[0].split(" ")
	x = [int(s[0]),int(s[1]),int(x[1]),int(x[2]),int(x[3])]
	list_.append(x)
	i=i+n

print(list_)
csvfile=open('data.csv','w')
obj=csv.writer(csvfile)
for data in list_:
	obj.writerow(data)
csvfile.close()

#print(type(list_[0][0]))
#########################################################
id_pos = {1:(0,0), 2:(0,1), 3:(0,2), 4:(0,3), 5:(0,4), 
		  6:(1,0), -104:(1,1), 8:(1,2), 9:(1,3), 10:(1,4), 
		  11:(2,0), 12:(2,1), -1407:(2,2), 14:(2,3), 15:(2,4), 
		  16:(3,0), 17:(3,1), 18:(3,2), 19:(3,3), 20:(3,4),
		  21:(4,0), 22:(4,1), 23:(4,2), 24:(4,3), 25:(4,4),}

# zero = ["-1047"] #(id,time)
# five = ["-104"]
zero = []
five = []

t = list_[0][1]
i = 0
for node in list_:
	if(i==0 and (node[1]-t)<30):
		zero.append(node[0])
	else:
		i=-1
		five.append(node[0])
predict = []

print(zero)
print(five)

x,y = 0,0

pos1 = id_pos[zero[0]]

for b in five:
	#print(pos2)
	pos2 = id_pos[b]
# 		
	d = (pos2[0]-pos1[0] , pos2[1]-pos1[1])
	x,y = x+d[0] , y+d[1]
	predict_pos = (pos2[0]+d[0],pos2[1]+d[1]) 
	predict.append(predict_pos)

x = x/len(five)
y = y/len(five)
if(y==0):
	print("Net predicted direction is: 90 degrees from "+str(pos1))

else:
	print("Net predicted direction is:"+str(math.degrees(math.atan(x/y))) +"degrees from "+str(pos1))
for a in predict:
	print(a)
