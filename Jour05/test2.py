x = int(input(" X width: "))
#y = int(input(" Y height: "))
print("diagonal_triangle : ") 
   
#y = (int(input(" Y height: ")))
for i in range(x):
    if i == 0 or i == x -1 :
        print("+" + "-"* x + "+" )
    #else:
        #for j in range(x):
            #if j == 0 or j == x -1:
                #j == j+1 and x/j+1  
    print("|" + "#"* (x -1 -i) + " "+ "#"* i + "|" )
   
            


    