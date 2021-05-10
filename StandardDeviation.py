import math
import sys

l = input ("Enter a Number: ")
l = int(l)
a = input ("Enter a Number: ")
a = int(a)
t = input ("Enter a Number: ")
t = int(t)
m = input ("Enter a Number: ")
m =int(m)

data = [l, a, t, m]

def sd_calc(data):
    n = len(data)

    if n <= 1:
        return 0.0

    mean, sd = avg_calc(data), 0.0

#calculate the standard deviation
    for el in data:
        sd += (float(el) - mean)**2
    sd = math.sqrt(sd / float(n-1))

    return sd

def avg_calc(ls):
    n, mean = len(ls), 0.0

    if n <= 1:
        return ls[0]

#calculate the average
    for el in ls:
        mean = mean + float(el)
    mean = mean / float(n)
    return mean

print("Standard Deviation: ",sd_calc(data))
