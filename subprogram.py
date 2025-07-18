import random
#my first subprogram (procedure)
def yeavyea():
    print("She likes to shopping.")
    print("She lives in Siem Reap.")
    print("She loves fries.")
#call my subprogram
yeavyea()
yeavyea()
yeavyea()

#my second subprogram (function)
def average(x, y):
    return (x + y) / 2
    
#call my subprogram
print(average(5, 5))

#procedure
def poavchou():
    print("poavchou loves sleeping!")
Poavchou()
poavchou()
poavchou()
poavchou()
poavchou()
poavchou()
poavchou()
poavchou()
poavchou()
poavchou()

#function
def sum(x ,y):
    return(x + y)
print(sum(2, 3))

def randomstudent():
    list = ["Yeavyea","Poavchou","William","Sereibot"]
    print(random.choice(list))
    
randomstudent()

def percentagecalculation(percentage, value):
    return (percentage * value) / 100
    
print(percentagecalculation(30, 70))
