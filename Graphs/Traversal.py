from collections import defaultdict


class Traversal:
	"""
	a class that performs different traversals on a graph
	"""
	def __init__(self):
		"""
		It defines an adjacency list for a bidirectional graph
		"""
		self.graph = defaultdict(list)
		self.size = 0

	def addEdge(self, u, v):
		"""
		Adds an edge between nodes in the graph
		:param u: 1st node
		:param v: 2nd node
		"""
		self.graph[u].append(v)
		self.graph[v].append(u)
		self.size = len(self.graph)

	def DFS(self, start=0):
		"""
		visit all nodes of a graph starting from a source node
		:param start: define the start node
		:return: path, a list containing the path traversed
		Note: for disconnected graph, pass seen and path as parameter, and perform dfs on all the unseen vertices
		Explanation of Time Complexity
		v1 + (incident edges) + v2 + (incident edges) + .... + vn + (incident edges)
		= (v1 + v2 + ... + vn) + [(incident_edges v1) + (incident_edges v2) + ... + (incident_edges vn)]
		= O(V) + O(2E) (--> remember incident_edges to node v' is its degree and sum of all degree = 2E)
		= O(V + E) (--> constant terms can be dropped)
		"""
		seen = set()
		stack = []
		path = []
		stack.append(start)

		while stack:
			node = stack.pop()
			if len(seen) == self.size:
				break

			# takes care of cycles
			if node in seen:
				continue

			seen.add(node)
			path.append(node)
			for next_node in self.graph[node]:
				stack.append(next_node)

		return path

	def BFS(self, start=0):
		"""
		visit all nodes of the graph starting from a source node
		:param start: define the start node
		:return: order, a list containing the order iun which the graph is traversed
		Time complexity is same as DFS
		"""
		queue = []
		seen = set()
		queue.append([start])
		order = []

		while queue:
			curr_path = queue.pop(0)
			if len(seen) == self.size:
				break

			last_node = curr_path[-1]

			if last_node not in seen:
				seen.add(last_node)
				order.append(last_node)
				for next_node in self.graph[last_node]:
					if next_node not in seen:
						queue.append(curr_path + [next_node])

		return order

