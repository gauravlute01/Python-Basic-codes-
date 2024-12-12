#hintspoints
#teams=["india","Australia"]
#50% probability winning teams to win the matches 
#which teams win match win 

from  numpy import random
teams=['EN','NL','PK','NE','AF','BA','IN','SA','NZ','AU']
c=0
winner1=[]
for i in range(len(teams)):
    for j in range(i+1,len(teams)):
        c+=1
        winner=random.choice([teams[i],teams[j]],p=[0.5,0.5])
        winner1.append(winner)
        #print(c,teams[i],"X",teams[j],"winner team=",winner)
#print(winner1)
winner2=[]
winner3=[]
#count_winner=[]
for i in range(len(teams)):
    n=winner1.count(teams[i])
    #print(teams[i],n)
    point=n*2
    winner2.append(point)
    #print("teams","no.win","points")
    a=(teams[i],point)
    winner3.append(a)
    #print(teams[i],n,point)
    #print(winner3)
d=dict(winner3)
#print(d)
#sort_winner3=sorted(d.values())
sort_winner3=dict(sorted(d.items(), key=lambda winner3_count: winner3_count[1],reverse=True)[:4])
#Top 4 teams
print(sort_winner3)
#semi final


