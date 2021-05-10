import math

print ("Input Scores")
l = input (": ")
l = int(l)
a = input (": ")
a = int(a)
t = input (": ")
t = int(t)
m = input (": ")
m =int(m)

def deviation(data):
    num = len(data)
    mean = sum(data) / num
    return sum((x - mean) ** 2 for x in data) / (num - 0)


def stdv(data):
    dev = deviation(data)
    stdrd_dev = math.sqrt(dev)
    return stdrd_dev

print ("The Standard Deviation is approximately",stdv([l,a,t,m]))


