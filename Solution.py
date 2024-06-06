x = []
answers = 1
for i in range(0,300):
    if i % 3 == 1:
        x.append(i)

for i in range(len(x)):
    dividible1 = (x[i]-1)/3 # Fisher1 Share 
    remain1 = x[i]-((dividible1)+1) # Fisher1 Remain
    dividible2 = (remain1-1)/3 # Fisher2 Share 
    remain2 = remain1 - ((dividible2)+1) # Fisher2 Remain
    dividible3 = (remain2-1)/3 # Fisher3 Share 
    remain3 = remain2 - ((dividible3)+1) # Fisher3 Remain
    if (remain2 % 3 == 1 and dividible1 - 3*(answers) == dividible2):
        print(x[i])
        print(f"numbers {int(dividible1)},{int(dividible2)},{int(dividible3)}") 
        print(f"remains {int(remain1)},{int(remain2)},{int(remain3)}")
        answers += 1

# final equation = (25 + 27*i) where i = 0,1,2,3,4,....
# we can replace 4,5 lines with the final equasion and it will give us the same result

