class MaxHeap:
	def __init__(self, heapsize):
		self.heapsize = heapsize
		self.realsize = 0
		self.maxheap = [None]*(heapsize+1)

	def push(self, val):
		self.realsize += 1
		if self.realsize > self.heapsize:
			print("Max Heap full...")
			self.realsize -= 1
		index = self.realsize
		parent = index//2
		self.maxheap[index] = val

		while index > 1 and self.maxheap[parent] < self.maxheap[index]:
			self.maxheap[parent], self.maxheap[index] = self.maxheap[index], self.maxheap[parent]
			index = parent
			parent = parent // 2

	def pop(self):
		if self.realsize < 1:
			print("Max Heap empty...")
			return None
		removed = self.maxheap[1]
		self.maxheap[1] = self.maxheap[self.realsize]
		self.realsize -= 1

		index = 1

		while index <= self.realsize:
			left = 2*index
			right = 2*index + 1
			if self.maxheap[index] < self.maxheap[left] or self.maxheap[index] < self.maxheap[right]:
				if self.maxheap[index] < self.maxheap[left]:
					self.maxheap[left], self.maxheap[index] = self.maxheap[index], self.maxheap[left]
					index = left
				else:
					self.maxheap[right], self.maxheap[index] = self.maxheap[index], self.maxheap[right]
					index = right
			else:
				break

		return removed
