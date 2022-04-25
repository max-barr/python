# Print all integers from 1-50
for i in range(1,51):
    print(i)

# Print all multiples of 5 from 5-1000
for i in range(5,1001,5):
    print(i)

# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(1,101):
    if i%10 == 0:
        print("Coding Dojo")
    elif i%5 == 0:
        print("Coding")
    else: print(i)
