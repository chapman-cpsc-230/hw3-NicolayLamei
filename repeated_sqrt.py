from math import sqrt

for n in range(1,60): #Here we are determing how many times we are pressing the Sqrt button
    r = 2.0 #Here we are determing that the number we are going to sqrt and square is going to be 2

    for i in range(n): #In this piece of code we are taking the sqrt of r (2)
        r = sqrt(r)

    for i in range(n): #In this piece of code we are squaring r again
        r = r**2

    print ("%d times sqrt and **2: %.16f" % (n,r)) #Here we are printing the results of square rooting and squaring r 60 times
