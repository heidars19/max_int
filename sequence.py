# Generates sequence where it adds up the last 3 numbers of the sequence to make the next number.

num1 = 0
num2 = 0
seq_num = 1

for i in range(0,n) :
    print(seq_num) 
    num1 = num2
    num2 = seq_num
    seq_num = seq_num + num1 + num2
    if seq_num == 1 :
        seq_num += 1