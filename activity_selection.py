//assuming that the activities are already sorted according to their finish time
def activities(start,finish):
    i=0
    print(i)
    for j in range(1,n):
        if(start[j]>=finish[i]):
            print(j)
            i=j
start=[]
finish=[]
n=int(input("enter the number of activities"))
for i in range(0,n):
    ele1=int(input("enter the starting time in ascending order of finishing time"))
    start.append(ele1)
    ele2=int(input("enter the finishing time in ascending order of finishing time"))
    finish.append(ele2)
print(start)
print(finish)
activities(start,finish)
