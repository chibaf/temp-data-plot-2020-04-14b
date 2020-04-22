import csv
import sys
import matplotlib.pyplot as plt

filename=sys.argv[1]  # name of input file = csv file

a=[]
with open(filename, newline='') as csvfile:  #read every row of csv file
  csv1=csv.reader(csvfile)
  for row in csv1:   # make matrix with row of csv
    a.append(map(float,row))
csvfile.close()
    
b=[list(x) for x in list(zip(*a))]; # transpose matrix

time=b[0];x1=b[1];x2=b[2];x3=b[3];x4=b[4];x5=b[5];x6=b[6];x7=b[7];  # time, second Tc, third Tc

l1,l2,l3,l4,l5,l6,l7 = "1","2","3","4","5","6","7"   # each lable of curve
fig, ax = plt.subplots()

ax.set_xlabel('time')  # x axis labele
ax.set_ylabel('temp')  # y axis labele
ax.set_title(r'pipe temps') # titlerange of y direction
#ax.plot(phi, y1, color=c1, label=l1)
#ax.plot(phi, y2, color=c2, label=l2)
#ax.plot(phi, y3, color=c3, label=l3)
ax.plot(x1, label=l1)
ax.plot(x2, label=l2)
ax.plot(x3, label=l3)
ax.plot(x4, label=l4)
ax.plot(x5, label=l5)
ax.plot(x6, label=l6)
ax.plot(x7, label=l7)
ax.legend(loc=0)    # legend of curves
fig.tight_layout()  # layout setting
plt.savefig('temps.png') # save plot
plt.show()
