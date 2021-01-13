# Gayle Shapley Algorithm
# Algorithms CS-310
# Hassaan Ahmad Waqar-22100137
# 23/10/2020
from queue import Queue
import time

def Get_data(name):
	filename = name +'.in'
	with open(filename, 'r') as input_file:
		first_line = input_file.readlines(1)
		first_line = list(map(lambda x:x.strip(),first_line))
		first_line = ' '.join(map(str, first_line)).split(" ") 
		first_line = list(map(int, first_line))
		
		num_hosp = first_line[0] # Number of Hospitals
		num_res = first_line[1] # Number of Students

		hosp_pref = {} # Hospital preference list initialized
		for i in range (0, num_hosp):
			hosp_pref[i] = []
		
		res_pref = {} # Student Preference list initialized
		for i in range (0, num_res):
			res_pref[i] = []

		second_line = input_file.readlines(1)
		second_line = list(map(lambda x:x.strip(),second_line))
		second_line = ' '.join(map(str, second_line)).split(" ") 
		hospital_slots = list(map(int, second_line)) # List having number of slots per hospital
		num_slots = sum(hospital_slots)
		
		Slots = Queue(maxsize = num_slots) # Queue that will store all vacant slots corresponding to Hospitals. E.g. 0-> slot of hospital 0
		h = 0
		for each in hospital_slots:
			for y in range(0,each):
				Slots.put(h)
			h = h+1

		h = 0
		for i in range(0, num_hosp): # Hospital preference filled up
			each_line = input_file.readlines(1)
			each_line = list(map(lambda x:x.strip(), each_line))
			each_line = ' '.join(map(str, each_line)).split(" ") 
			each_line = list(map(int, each_line))
			for each_value in each_line:
				hosp_pref[h].append(each_value)
			h = h + 1


		r = 0
		for i in range(0, num_res): # Residents preference filled up
			each_line = input_file.readlines(1)
			each_line = list(map(lambda x:x.strip(), each_line))
			each_line = ' '.join(map(str, each_line)).split(" ") 
			each_line = list(map(int, each_line))
			for each_value in each_line:
				res_pref[r].append(each_value)
			r = r + 1
	Resident_Match = [-1] * num_res
	
	return hosp_pref, res_pref, Slots, Resident_Match
	# All Data Structures required created. Hosptital and Resident Preference Dictionaries, Hospital Slots List, SLots Queue, Resident Match List 

def main():
	val = input("Enter filename (only name, not extension E.g. 1-5-5): ")  
	start = time.time()
	hosp_pref, res_pref, Slots, Resident_Match = Get_data(val)
	
	# While some slot remains
	while(Slots.empty() == False): 
		current_hospital = Slots.get()
		match = False
		while(match == False):
			current_student = hosp_pref[current_hospital][0]
			if(Resident_Match[current_student] == -1): # Not matched before
				Resident_Match[current_student] = current_hospital
				del hosp_pref[current_hospital][0]
				match = True
			else: # Resident gets a better offer
				get_matched_hosp = Resident_Match[current_student]
				get_index_of_matched = res_pref[current_student].index(get_matched_hosp)
				get_index_of_offer =  res_pref[current_student].index(current_hospital)
				if(get_index_of_offer < get_index_of_matched):
					Slots.put(get_matched_hosp)
					Resident_Match[current_student] = current_hospital
					del hosp_pref[current_hospital][0]
					match = True
				else: # Resident rejects the offer
					del hosp_pref[current_hospital][0] 
					match = False
	
	Resident_Match = ' '.join(map(str, Resident_Match))
	outname = val+'.out'
	with open(outname, 'w') as output_file:
		output_file.write(Resident_Match)

	end = time.time()
	total = end-start
	#print(total)

main()

# Code used to plot graph of Hospitals and Execution time 

# import numpy as np
# from numpy import *
# import sys
# import time 
# import matplotlib.pyplot as plt

# # Code for plotting graph of Number of Hospitals and Execution time
# # For each value of hospital, code was run three times and the average time was taken
# hospitals = [1,3,40,80,160,320]
# time = [0.995,1.998, 5.983, 18.949, 74.399, 295.661]
# fig,plots = plt.subplots()
# plots.plot(hospitals, time)
# plots.set(xlabel = 'Number of Hospitals', ylabel='Execution Time (in ms)', title = 'Trend of Number of Hospitals with Execution Time')
# plots.grid()
# fig.savefig("time.png")
