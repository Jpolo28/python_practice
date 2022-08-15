def hello():
    print("Hello!")
hello()
def pack(Iphone, Pc, Switch):
    pack = ["Iphone", "Pc", "Switch"]
    print(pack)
print(pack("Iphone", "Pc", "Switch"))

food = ["salad", "pasta", "pizza", "canoli"]   
def eat_lunch(food):
    if len(food) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(food)): 
            if i == 0:
                print("First I ate " + food[0])
            elif i != 0:
                print("Next I ate " + food[i]) 
        

 

print (eat_lunch(food))