__author__ = 'Sam Haycraft'

num = int(input('Enter number of iterations: '))

fibs = [1, 1]
for i in range(2, num):
    fibs.append(fibs[i-1]+fibs[i-2])

print fibs
ratio = float(fibs.pop())/float(fibs.pop())
print 'ratio = ' + str(ratio)

kilo = float(input('Enter kilometers: '))
miles_actual = kilo * 1.60934
miles_fib = kilo * ratio
diff = abs(miles_actual - miles_fib)

print 'Actual miles = ' + str(miles_actual)
print 'Calculated miles with golden ration= ' + str(miles_fib)
print 'Residual = ' + str(diff)