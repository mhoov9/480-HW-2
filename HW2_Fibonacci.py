#This function takes a number x and returns the Fibonacci number
#that belongs to the xth term in the Fibonacci sequence

def fib(x):
    if x == 1:
	    return 0
    if x == 2:
	    return 1
    return fib(x-1) + fib(x-2)


#fib_seq returns a list of the Fibonacci sequence n terms long
#starting from 0

def fib_seq(n):
    i = 1
    fib_list = []
    while i <= n:
	    fib_list.append(fib(i))
	    i += 1
    return fib_list

#The next function uses the Fibonacci list that was previously constructed
#to approximate the Golden Ratio. The larger the number, the better
#the approximation will be. 

def approx_goldratio(n):
    approx = float(((fib_seq(n))[n-1]))/float(((fib_seq(n))[n-2]))
    print ((fib_seq(n))[n-1])
    print ((fib_seq(n))[n-2])
    return approx
