__author__ = 'Sam Haycraft'

num = int(input('Enter number of iterations: '))

fibs = [1, 1]
for i in range(2, num):
    fibs.append(fibs[i-1]+fibs[i-2])

print fibs
print 'ratio = ' + str(float(fibs.pop())/float(fibs.pop()))