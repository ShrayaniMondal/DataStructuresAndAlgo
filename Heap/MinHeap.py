class MinHeap:
	def __init__(self, heapsize):
		self.heapsize = heapsize
		self.realsize = 0
		self.minheap = [None]*(heapsize+1)

	def push(self, val):
		self.realsize += 1
		if self.realsize > self.heapsize:
			print("Min Heap full...")
			self.realsize -= 1
		index = self.realsize
		parent = index//2
		self.minheap[index] = val

		while index > 1 and self.minheap[parent] > self.minheap[index]:
			self.minheap[parent], self.minheap[index] = self.minheap[index], self.minheap[parent]
			index = parent
			parent = parent//2

	def pop(self):
		if self.realsize < 1:
			print("Min Heap empty...")
			return None
		removed = self.minheap[1]
		self.minheap[1] = self.minheap[self.realsize]
		self.realsize -= 1

		index = 1

		while index >= self.realsize:
			left = 2*index
			right = 2*index + 1
			if self.minheap[index] > self.minheap[left] or self.minheap[index] > self.minheap[right]:
				if self.minheap[index] > self.minheap[left]:
					self.minheap[left], self.minheap[index] = self.minheap[index], self.minheap[left]
					index = left
				else:
					self.minheap[right], self.minheap[index] = self.minheap[right], self.minheap[left]
					index = right
			else:
				break
		return removed

