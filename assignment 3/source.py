"""This project created by t2k:-Tushar Tailor"""

"""
#code 1:-This code take input and stored them in dictionary. 
x=int(input("Enter no. of players:-"))
dd={}
for i in range(x):
    def li():
        y={}
        y["Name"]=input("enter name:")
        y["Role"]=input("Enter role(bat/bol):")
        if y["Role"]=="bat":
            y["Runs"]=int(input("Enter runs:"))
            y["4's"]=int(input("enter no. of 4 hit:"))
            y["6's"]=int(input("Enter no. of 6 hit:"))
            y["Balls"]=int(input("enter no. of balls played:"))
        else:
            y["wkts"]=int(input("enter no. of wkts:"))
            y["Overs"]=int(input("enter no. of overs:"))
            y["runs"]=int(input("enter no. of runs:"))
        y["feild"]=int(input("enter no. of feild(catch/stumping/run out)"))
    
        return y
    m=li()
    dd[i+1]=m
for i in range(x):
    print(dd[i+1])
"""
import score
#After storing......i take examples of it.....
p1={'name':'Tushar', 'role':'bat', 'runs':150, '4':12, '6':3, 'balls':119, 'field':5} 
p2={'name':'Vishnu', 'role':'bat', 'runs':122, '4':9, '6':2, 'balls':99, 'field':2} 
p3={'name':'Tony', 'role':'bowl', 'wkts':2, 'overs':5, 'runs':50, 'field':3} 
p4={'name':'Bolt', 'role':'bowl', 'wkts':3, 'overs':10, 'runs':34, 'field':0} 
p5={'name':'Sanju', 'role':'bowl', 'wkts':0, 'overs':1, 'runs':67, 'field':1}

l1=[p1,p2,p3,p4,p5]
print(dir(score))
pp={}
for i in l1:
    if i['role']=="bat":
        point=score.batscore(i)
        pp[i['name']]=point
        print("name:{} and batscore:{}".format(i['name'],point))
    else:
        point=score.balscore(i)
        pp[i['name']]=point
        print("name:{} and balscore:{}".format(i['name'],point))

best=max(pp,key=pp.get)
score=max(pp.values())
print("Player of the match is {} and he score {} points.".format(best,score))




    
    

        
