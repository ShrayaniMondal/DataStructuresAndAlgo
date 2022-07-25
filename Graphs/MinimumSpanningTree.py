from collections import defaultdict
import heapq
from DisjointSet import DisjointSet

class Edge:
	"""
	a class that defines what an edge is
	"""
	def __init__(self, u, v, wt):
		"""
		:param u: 1st node
		:param v: 2nd node
		:param wt: the weight of the edge
		"""
		self.vertex1 = u
		self.vertex2 = v
		self.weight = wt

	def __lt__(self, other):
		"""
		:param other: another object of type Edge
		:return: a boolean
		"""
		return self.weight < other.weight


class MSP:
	"""
	a class that finds MSP using Prim's and Kruskal's Algorithm
	"""
	def __init__(self):
		"""
		It defines the bidirectional graph
		"""
		self.nodes = set()
		self.graph = defaultdict(list)
		self.size = 0

	def addEdge(self, u, v, weight):
		"""
		Adds an edge between nodes in the graph
		:param weight: the weight of the edge
		:param u: 1st node
		:param v: 2nd node
		"""
		self.nodes.add(u)
		self.nodes.add(v)

		edge = Edge(u, v, weight)
		self.graph[u].append(edge)
		self.graph[v].append(edge)
		self.size = len(self.nodes)

	def Prim(self):
		"""
		:return min_cost: return the weight/cost of minimum spanning tree
		Explanation of Time Complexity
		Much like BFS we need to traverse through all the vertices atleast once
		and add the outgoing edges to the minheap
		v1 + (incident edges) + v2 + (incident edges) + .... + vn + (incident edges)
		= (v1 + v2 + ... + vn) + [(incident_edges v1) + (incident_edges v2) + ... + (incident_edges vn)]
		= O(V) + O(2E) (--> remember incident_edges to node v' is its degree and sum of all degree = 2E)
		= O(V + E) (--> constant terms can be dropped)

		And minheap operations take O(log(N)) time, where N is the number of components in the heap
		add v1 ---> atmost (v1-1) edges
		add v2 --->	 atmost [(v1-1) + (v2-1)-1] edges	(exclude v2 to v1 edge)
		.
		.
		.
		add v(n-1) ---> atmost [(v1-1) + (v2-1)-1 + ... + 1] edges

		N = atmost O(v1-1 + v2-2 + ... +1) components in the minheap.
		= O(V^2) components in the minheap.
		So the operations take O(log(V^2)) time at most. = O(2log(V)) = O(log(V))

		Hence, time complexity is O((V+E).log(V))
		"""
		min_cost = 0

		# initialize all the edges that have not been visited
		not_visited = []
		# all vertices that have been visited
		visited = set()

		# choose an arbitrary starting node and add it to visited
		start = 0
		visited.add(start)
		counter = 1 #since one vertex has been visited just now

		# add all the outgoing edges from the start to not_visited
		for edge in self.graph[start]:
			not_visited.append(edge)

		# now heapify the outgoing edges
		heapq.heapify(not_visited)

		while not_visited and counter < self.size:
			edge = heapq.heappop(not_visited)
			vertex2 = edge.vertex2
			cost = edge.weight

			if vertex2 not in visited:
				min_cost += cost
				visited.add(vertex2)
				counter += 1
				for edge in self.graph[vertex2]:
					if edge.vertex2 not in visited:
						heapq.heappush(not_visited, edge)

		return min_cost

	def Kruskal(self):
		"""
		:return min_cost: return the weight/cost of minimum spanning tree
		Explanation of Time Complexity
		Sorting takes O(E.log(E)) time.
		Each disjoint set operation(connected() and union()) takes O(alpha(V)). So a total of O(E.alpha(V))
		where alpha is the inverse Ackerman function and  O(alpha (V)) is regarded as O(1) on average
		Hence, time complexity is O(E.log(E))
		"""
		min_cost = 0

		edge_list = [edge for edges in self.graph.values() for edge in edges]
		edge_list.sort()

		ds = DisjointSet(self.size)

		counter = 0

		for edge in edge_list:
			if not ds.connected(edge.vertex1, edge.vertex2) and counter < self.size:
				ds.union(edge.vertex1, edge.vertex2)
				min_cost += edge.weight
		return min_cost





