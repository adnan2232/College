
def calculateDifference(queue, head, diff):
	for i in range(len(diff)):
		diff[i][0] = abs(queue[i] - head)
	

def findMin(diff):

	index = -1
	minimum = 999999999

	for i in range(len(diff)):
		if (not diff[i][1] and
				minimum > diff[i][0]):
			minimum = diff[i][0]
			index = i
	return index
	
def shortestSeekTimeFirst(request, head):			
	if (len(request) == 0):
		return
		
	l = len(request)
	diff = [0] * l
		

	for i in range(l):
		diff[i] = [0, 0]
		
	
	seek_count = 0
		

	seek_sequence = [0] * (l + 1)
		
	for i in range(l):
		seek_sequence[i] = head
		calculateDifference(request, head, diff)
		index = findMin(diff)
			
		diff[index][1] = True
			
			
		seek_count += diff[index][0]
			
	
		head = request[index]
	

	seek_sequence[len(seek_sequence) - 1] = head
		
	print("Total number of seek operations =",
								seek_count)
														
	print("Seek Sequence is")
	
	for i in range(l + 1):
		print(seek_sequence[i])
	

if __name__ =="__main__":
    print("55_Adnan Shaikh")
    proc = list(map(int,input("Enter requests: ").strip().split()))
    head = int(input("Enter the head position: "))
    shortestSeekTimeFirst(proc, head)
	

