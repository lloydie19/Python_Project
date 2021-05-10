import math
import statistics

print ("Enter the List of Numbers")
a = input ("a : ")
a = int(a)
b = input ("b : ")
b = int(b)
c = input ("c : ")
c = int(c)
d = input ("d : ")
d =int(d)

number_list = [a,b,c,d]
#calculates the Sample Average
avg = sum(number_list)/len(number_list)
print("The Average is equal to:", avg)

#Calculates the mean
def average_Cal(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num / len(num)
    return avg

print("The Sample Average equal to:", average_Cal(number_list))

#calculates the standard Dev
def deviation(data):
    num = len(data)
    mean = sum(data) / num
    return sum((x - mean) ** 2 for x in data) / (num - 0)


def stdv(data):
    dev = deviation(data)
    stdrd_dev = math.sqrt(dev)
    return stdrd_dev

print("The Standard deviation is equal to:", stdv(number_list))

l= (statistics.mean(number_list)-(average_Cal(number_list)))
Z= (l/stdv(number_list))

print ("Z-test is equal to: ", Z)
