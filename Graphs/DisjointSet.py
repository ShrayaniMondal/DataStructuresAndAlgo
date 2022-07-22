class DisjointSet:
	"""
	an optimized class that encapsulates the methods for creating a disjoint set with time complexity for
	Creating the Union-find Constructor: O(N)
	Find : O(alpha(N)) where alpha is the inverse Ackerman function
	Union : O(alpha(N)) where alpha is the inverse Ackerman function
	Connected : O(alpha(N)) where alpha is the inverse Ackerman function
	Note : O(alpha (N)) is regarded as O(1) on average.
	"""
	def __init__(self, size):
		"""
		Initializes root and rank for each node of the Disjoint Set
		:param size: the number of nodes in the disjoint set
		"""
		self.root = [i for i in range(size)]
		self.rank = [1 for i in range(size)]

	def find(self, x):
		"""
		:param x: the node whose root we need to find
		:return: the root of node x
		"""
		if x != self.root[x]:
			self.root[x] = self.find(self.root[x])
		return self.root[x]

	def union(self, x, y):
		"""
		perform union operation on node x and y
		:param x: 1st node
		:param y: 2nd node
		:return: None
		"""
		rootx = self.find(x)
		rooty = self.find(y)

		if rootx != rooty:
			if self.rank[rootx] > self.rank[rooty]:
				self.root[rooty] = rootx
			elif self.rank[rooty] > self.rank[rootx]:
				self.root[rootx] = rooty
			else:
				self.root[rooty] = rootx
				self.rank[rootx] += 1

	def connected(self, x, y):
		"""
		:param x: 1st node
		:param y: 2nd node
		:return: True if nodes x and y are connected
		"""
		return self.find(x) == self.find(y)
