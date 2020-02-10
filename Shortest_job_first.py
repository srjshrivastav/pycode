from prettytable import PrettyTable
table=PrettyTable()
n=int(input(("Enter no of process :")))
process={}
w_t={}
t_w_t=0
tat={}
ct=0
for i in range(n):
    process["P{0}".format(i)]=int(input("Enter Burst Time for P{0} :".format(i)))

sorted_process=sorted(process.items(), key = 
             lambda kv:(kv[1], kv[0])) 
for i in sorted_process:
    print("|",i[0],end="")
print("|\n%d"%(ct),end="   ")
for i in sorted_process:
    ct+=i[1]
    tat[i[0]]=ct
    w_t[i[0]]=ct-i[1]
    t_w_t+=w_t[i[0]]
    print(ct,end="   ")
table.field_names=["PID","Arriva Time","Burst Time","Waiting Time","Turn Around"]
for process,bt in process.items():
    table.add_row([process,0,bt,w_t[process],tat[process]])
print(table)
print("ThroughPut :",n/ct)
print("Avg. waiting time :",round(t_w_t/n,2))
    


    