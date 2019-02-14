Number = int(input())    
Rev = 0    
while(Number > 0):    
    Reminder = Number %10    
    Rev = (Rev*10) + Reminder    
    Number = Number //10    
print(Rev)   
