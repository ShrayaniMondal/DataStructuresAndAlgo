from collections import defaultdict


class TopologicalSort:
	"""
	a class that performs Topological Sorting using Kahn's ALgorithm
	(a linear sorting based on the required ordering between vertices in directed acyclic graphs)
	"""
	def __init__(self):
		"""
		It defines the adjacency list for graph
		"""
		self.nodes = set()
		self.graph = defaultdict(list)
		self.size = 0

	def addEdge(self, u, v):
		"""
		Adds an edge between nodes in the graph
		:param u: 1st node
		:param v: 2nd node
		"""
		self.nodes.add(u)
		self.nodes.add(v)

		self.graph[u].append(v)
		self.size = len(self.nodes)

	def Kahn(self):

		indegree = {key: 0 for key in self.nodes}
		for values in self.graph.values():
			for v in values:
				indegree[v] += 1

		visited = []

		queue = []
		for k,v in indegree.items():
			if v == 0:
				queue.append(k)

		if not queue:
			return visited

		while queue:
			node = queue.pop()
			visited.append(node)

			for neighbour in self.graph[node]:
				indegree[neighbour] -= 1
				if indegree[neighbour] == 0:
					queue.append(neighbour)

		return visited


