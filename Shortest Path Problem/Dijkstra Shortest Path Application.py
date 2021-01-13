# HASSAAN AHMAD WAQAR
# 22100137
# Algorithms A2

# Dijkstra missing a few conditions and therefore not giving proper paths
# Adjacency list maintained
# Heap maintained
# Dijkstra attempted for Source airport and intermediate airports. But not fully implemented



class Create_Heap:

	def __init__(self):

		self.heap_size = 0
		self.heap = []
		self.heap.append([None, None, None, None, None, -10000000000]) # heap of lists # [dest, flight name, flight code, start time, end time, weights] -> sort on weights
		self.root = 1


	def get_parent_index(self, val):
		return int( (val)/2 ) 
	def get_right_index(self, val):
		return int( (2*val)+1)
	def get_left_index(self, val):
		return int( (2*val) )
	def insert(self, val):
		self.heap_size = self.heap_size + 1
		self.heap.append(val)
		this_node = self.heap_size
		#print(self.heap)
		#print(self.heap[1])
		
		# Readjust
		while(self.heap[this_node][5] < self.heap[self.get_parent_index(this_node)][5]): # swap required
			temp = self.heap[self.get_parent_index(this_node)]
			self.heap[self.get_parent_index(this_node)] = self.heap[this_node]
			self.heap[this_node] = temp
			this_node = self.get_parent_index(this_node)	


	def check_for_leaf(self, val):
		if(val >= int(self.heap_size/2)  and val <= self.heap_size):
			return True
		else:
			return False

	def Restore(self, val): 
		if(self.check_for_leaf(val) == False):
			if(self.heap[val][5] > self.heap[self.get_left_index(val)][5] or self.heap[val][5] > self.heap[self.get_right_index(val)][5] ):
				if(self.heap[self.get_left_index(val)][5] < self.heap[self.get_right_index(val)][5] ): # swapping required
					
					temp = self.heap[self.get_left_index(val)]
					self.heap[self.get_left_index(val)] = self.heap[val]
					self.heap[val] = temp

					self.Restore(self.get_left_index(val))
				else: # swapping required
					
					temp = self.heap[self.get_right_index(val)]
					self.heap[self.get_right_index(val)] = self.heap[val]
					self.heap[val] = temp
					
					self.Restore(self.get_right_index(val)) # check if new right child is still greater than its children

	def IsEmpty(self):
		if(self.heap_size == 0):
			return True
		else:
			return False

	def Remove(self):
		get_root = self.heap[self.root]
		self.heap[self.root] = self.heap[self.heap_size]
		self.heap_size = self.heap_size - 1
		
		self.Restore(self.root)
		
		return get_root

def Get_data():

	offsets = {} 
	AL = {} # adjacency list
	route = {}
	Parents = {}
	Visited = {}
	Weights = {}

	with open('airport-data.txt', 'r') as input_file:
		first_line = input_file.readlines(1)
		first_line = list(map(lambda x:x.strip(),first_line))
		first_line = list(map(int, first_line))
		vertices = first_line[0] # Number of vertices known
				
		for each in range(0, vertices):
			first_line = input_file.readlines(1)
			first_line = list(map(lambda x:x.strip(),first_line))
			first_line = ' '.join(map(str, first_line)).split('\t') 
			offsets[first_line[0]] = (int(first_line[1].replace('-', ''))/100) * 60 # Need to add this offset in minutes to locat time in minutes
			AL[first_line[0]] = {}
			route[first_line[0]] = [None, None, None, None, None, 100000000]
			Parents[first_line[0]] = None
			Visited[first_line[0]] = 0
			Weights[first_line[0]] = 100000000


		#print(offsets)

	# with open('template.txt', 'r') as input_file:

	with open('flight-data.txt', 'r') as input_file:
		first_line = input_file.readlines()
		first_line = list(map(lambda x:x.strip(),first_line))
		length = len(first_line)-1

	with open('flight-data.txt', 'r') as input_file:
		count = 0
		while(count<length):
			first_line = input_file.readlines(1)
			first_line = list(map(lambda x:x.strip(),first_line))
			first_line = ' '.join(map(str, first_line)).split('\t') 
			#print(first_line)

			airlines = first_line[0]
			airlines_code = first_line[1]
			source = first_line[2]
			dest = first_line[5]
			local_start = int(first_line[3])
			if(first_line[4] == 'A'):
				start_time_in_min = int(local_start/100)*60 + local_start%100
			elif(first_line[4] == 'P'):
				start_time_in_min = int(local_start/100)*60 + (local_start%100) + (12*60)
			elif(first_line[4] == 'N'):
				start_time_in_min = 12*60
			
			offset_to_add = offsets[source]
			start_time_in_min = start_time_in_min + offset_to_add # This is in GMT

			local_end = int(first_line[6])
			if(first_line[7] == 'A'):
				end_time_in_min = int(local_end/100)*60 + local_end%100
			elif(first_line[7] == 'P'):
				end_time_in_min = int(local_end/100)*60 + (local_end%100) + (12*60)
			elif(first_line[7] == 'N'):
				end_time_in_min = 12*60

			offset_to_add = offsets[dest]
			end_time_in_min = end_time_in_min + offset_to_add # This is in GMT

			duration = (end_time_in_min - start_time_in_min) 
			if(duration < 0):
				duration = duration + 1440
			start_time_in_min = start_time_in_min % 1440
			end_time_in_min = end_time_in_min % 1440

			if(dest not in AL[source]):
				AL[source][dest]=[]
			list_to_add = [dest, airlines, airlines_code, start_time_in_min,end_time_in_min,duration]
			AL[source][dest].append(list_to_add)
			count = count + 1
		
	return vertices, offsets, AL, route, Parents, Visited, Weights

def dijkstra(route, Parents, source_node, start_time, user_wait, user_dest, AL, Visited, Weights):
	
	# weights, Visited, Parents
	# print(Weights)
	# print(Visited)
	# print(Parents)

	# [dest, flight name, flight code, start time, end time, duration of flight]

	Bigheap = Create_Heap()

	current_node = source_node 
	Weights[source_node] = 0
	Visited[source_node] = 1

	start_atleast = 120 + start_time

	# catering for source to immediate neighbors
	for keys in AL[current_node]:
		for values in AL[current_node][keys]:
			if(values[3] > start_atleast):
				total_time = (values[3] - start_time) + values[5] # time constaint 1
				copy = values
				copy[5] = total_time
				Bigheap.insert(copy)
				if(Weights[keys] > total_time):
					Weights[keys] = total_time
					list_to_append = values
					list_to_append.append(current_node) # [dest, flight name, flight code, start time, end time, updated weights, parent]
					Parents[keys] = list_to_append

	# catering for intermediate nodes
	while(Bigheap.IsEmpty == False):
		extracted = Bigheap.Remove()
		dest = extracted[0]
	
		Visited[dest] = 1
		start_atleast = 60 + extracted[4]

		for keys in AL[dest]:
			for vals in AL[dest][keys]:
				if(Visited[keys] == 0):
					if(vals[3] > start_atleast):
						total_time = (values[3] - extracted[4]) + vals[5] + extracted[5] # Time constraint 2
						copy = vals
						copy[5] = total_time
						Bigheap.insert(copy)
						if(Weights[keys] > total_time):
							Weights[keys] = total_time
							list_to_append = values
							values.append(dest) # [dest, flight name, flight code, start time, end time, updated weights, parent]
							Parents[keys] = list_to_append

		if(dest == user_dest):
			break


	#print(route)
	print(Parents)
	#print(Weights)
	#print(Visited)


def main():
	vertices, offsets, AL, route, Parents, Visited, Weights = Get_data()
	#print(AL)
	val = input("Enter flight data: ")
	user_in = list(val.split(" "))
	#print(user_in)

	source_node = user_in[0]
	user_dest = user_in[1]
	start_in = int(user_in[2])
	conv = user_in[3]
	stay = int(user_in[4])

	if(conv == 'A'):
		time_to = int(start_in/100)*60 + start_in%100
	elif(conv == 'P'):
		time_to = int(start_in/100)*60 + (start_in%100) + (12*60)
	elif(conv == 'N'):
		time_to = 12*60

	offset_to_add = offsets[source_node]
	time_to = time_to + offset_to_add # This is in GMT

	# print(start_time)

	dijkstra(route, Parents, source_node, time_to, stay, user_dest, AL ,Visited, Weights)

	print("...")
	print(" Dijkstra algorithm not impletemented successfully (some conditions missing) ")
	print(" Adjacency lists maintained properly, Heap Created, catered for Source and intermediate airports but corner cases missing apparently ")
	
main()
