import random
import string
import time
from math import ceil


def Addition(num_one, num_two):
	# num_one = "2345"
	# num_two = "123"
	storage = ""
	carry = 0 
	if(len(num_one) == len(num_two)):
		pass
	elif(len(num_one) < len(num_two)):
		num_one = num_one.rjust(len(num_two),"0")
	elif(len(num_one) > len(num_two)):
		num_two = num_two.rjust(len(num_one),"0")
	for i in range(len(num_two)-1, -1, -1):
		lower = int(num_two[i])
		upper = int(num_one[i])
		summ = lower + upper
		summ = summ + carry
		if(i != 0):
			store = summ % 10
			carry = int(summ/10)
		else:
			store = summ
		storage = str(store) + storage

	return storage

def Subtraction(num_one, num_two):
	if(len(num_one) > len(num_two)):
		greater = num_one
		smaller = num_two
	elif(len(num_one) < len(num_two)):
		greater = num_two
		smaller = num_one
	else:
		for i in range(len(num_one)):
			one_digit = int(num_one[i])
			two_digit = int(num_two[i])
			if(one_digit> two_digit):
				greater = num_one
				smaller = num_two
				break
			elif(one_digit< two_digit):
				greater = num_two
				smaller = num_one
				break
			else:
				greater = num_one
				smaller = num_two

	if(len(smaller) < len(greater)):
		smaller = smaller.rjust(len(greater), "0")

	to_send = ""
	check = 0
	for i in range(len(greater)-1, -1, -1):
		upper = int(greater[i])
		lower = int(smaller[i])
		if(check == 1):
			upper = upper - 1
			check = 0
		if(upper < lower):
			check = 1
			upper = upper + 10
		storage = upper - lower
		to_send = str(storage) + to_send
	to_send = to_send.lstrip('0')
	return to_send

def K(num_one, num_two):
	n = min(len(num_one), len(num_two))
	m = ceil(n/2)

	if( (len(num_one) == 1) or (len(num_two)==1) ):
		mult = int(num_one) * int(num_two)
		return str(mult)

	a = len(num_one) - m
	b = len(num_two) - m
	x_high = num_one[:a]
	x_low = num_one[a:]
	y_high = num_two[:b]
	y_low = num_two[b:]

	e = K(x_high,y_high)
	f = K(x_low,y_low)
	g = K(Addition(x_high,x_low), Addition(y_high,y_low))
	# subtract = str(int(g) - int(e) - int(f))
	h = Subtraction(g,e)
	j = Subtraction(h,f)

	sum_one = e.ljust(len(e)+(2*m),"0")
	sum_two = j.ljust(len(j)+m,"0")
	sum_three = Addition(sum_one,sum_two)
	sum_four = Addition(sum_three,f)
	return sum_four

def main():

	# Assumption for Karatsuba: Size of both number is the same. 
	x = input("Type of algo ")
	first = input("Enter first number ")
	second = input("Enter Second number ")

	# Number generation through random strings concantenation for plotting graphs with respect to digits
	#first = ''.join(random.choice(string.digits) for num in range(10000))
	#second = ''.join(random.choice(string.digits) for num in range(10000))

	# Code snippet for graph. Plotted in Jupyter notebooks 
	# digits = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000] 
	# time_B = [3018, 12740, 27579, 53567, 88160, 209594, 371073, 530138,  786361, 1248028] 
	# time_D = [1185, 3534, 6803, 10719, 16223, 20167, 27320, 34265, 40917, 50280] 
	# plt.figure(figsize=(15,10))
	# plt.plot(digits,time_B, label ='Brute Force O(n^2)')
	# plt.plot(digits,time_D, label ='Divide and Conquer O(1.59)')
	# plt.title('Integer Multiplication Algorithm Runtime vs Number of digits')
	# plt.xlabel('Number of Digits')
	# plt.ylabel('Time in milliseconds')
	# plt.legend()
	# plt.show()

	#print(first)
	#print(second)

	if(x == 'B'):
		start = time.time()
		global_sum = ""
		zero_counter = 0

		for index in range(len(second)-1, -1, -1):
			lower_pick = int(second[index])
			summ = ""
			carry = 0
			for inner in range(len(first)-1, -1, -1):
				upper_pick = int(first[inner])
				mult = lower_pick * upper_pick
				mult = mult + carry
				if(inner != 0 ):
					store = mult % 10
					carry = int(mult/10)
				else:
					store = mult
				summ = str(store) + summ
			summ = summ.ljust(len(summ)+zero_counter, "0")
			zero_counter = zero_counter + 1
			# Call Function now
			global_sum = Addition(global_sum, summ)
		print("Result", global_sum)
		end = time.time()
		time_taken = (end - start)*1000
		print("Time taken in ms", time_taken)
	
	elif(x == 'D'):
		start = time.time()
		result = K(first, second)
		end = time.time()
		time_taken = (end - start)*1000
		print("Result", result)
		print("Time taken in ms", time_taken)
	
main()

