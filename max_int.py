#Algorithm for keeping the maximum number from input numbers 

max_int = 0
while num_int >= 0 :
    if max_int < num_int:
        max_int = num_int
    num_int = int(input("Input a number: "))
    
    