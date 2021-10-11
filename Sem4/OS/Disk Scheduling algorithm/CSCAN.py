
def CSCAN(arr, head,disk_size,size):

	seek_count = 0
	distance = 0
	cur_track = 0
	left = []
	right = []
	seek_sequence = []


	left.append(0)
	right.append(disk_size - 1)


	for i in range(size):
		if (arr[i] < head):
			left.append(arr[i])
		if (arr[i] > head):
			right.append(arr[i])


	left.sort()
	right.sort()

	for i in range(len(right)):
		cur_track = right[i]


		seek_sequence.append(cur_track)

		distance = abs(cur_track - head)


		seek_count += distance


		head = cur_track


	head = 0


	seek_count += (disk_size - 1)


	for i in range(len(left)):
		cur_track = left[i]


		seek_sequence.append(cur_track)

		
		distance = abs(cur_track - head)

	
		seek_count += distance

	
		head = cur_track

	print("Total number of seek operations =",
		seek_count)
	print("Seek Sequence is")
	print(*seek_sequence, sep="\n")





if __name__ == "__main__":
    print("55_Adnan Shaikh")
    arr = list(map(int,input("Enter requests: ").strip().split()))
    head = int(input("Enter head position: "))
    disk_size = int(input("Enter ending position of disk: ")) + 1
    print("Initial position of head:", head)

    CSCAN(arr, head, disk_size,len(arr))