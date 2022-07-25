from collections import defaultdict
import heapq


class SingleSourceShortestPath:
	"""
	a class that finds Single Source Shortest Path in a directed graph using
	1. Dijkstra's Algorithm
	2. Bellman-Ford Algorithm
	Note: there is no solution for graphs with negative cycles.
	"""
	def __init__(self):
		"""
		It defines the adjacency list for graph
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
		self.graph[u].append([weight, v])
		self.size = len(self.nodes)

	def Dijkstra(self, source):
		"""
		:param source: starting node
		:return: return the shortest paths from source to every other node
		Note: 1. won't work for graphs with -ve weights
			2. not super efficient when dealing k stops in between
		Explanation of Time Complexity
		every edge gets added atmost once to the edges minheap
		and operations in minheap take O(log(E)) time
		shortes_path dictionary contruction takes O(V) time

		Therefore, overall O(V + Elog(E)) time complexity
		"""
		shortest_path = {key: [float("inf"), None] for key in self.graph.keys()}
		shortest_path[source] = [0, None]
		edges = [(0, source)]
		visited = set()

		while edges:
			curr_weight, curr_vertex = heapq.heappop(edges)
			if curr_vertex in visited:
				continue
			visited.add(curr_vertex)

			for neighbour, dist in self.graph[curr_vertex]:
				if neighbour in visited:
					continue
				if shortest_path[neighbour] > curr_weight + dist:
					shortest_path[neighbour] = [curr_weight + dist, curr_vertex]
					heapq.heappush(edges, (curr_weight + dist, neighbour))

		if len(visited) != self.size:
			print("Not all nodes could be reached from source!!!")
		return shortest_path

	def BellmanFord(self, source):
		"""
		:param source: the starting node
		:return: shortest distances from source node to any node with k stops in between
		Explanation of Time Complexity:
		Edge relaxation operation is done E times for each pass.
		The number of passes is (V-1)
		Overall time complexity = O(V.E)
		"""
		# make a list of edges of format (u,v,wt)
		edges = []
		for u in self.graph:
			edges = edges + [(u, v, weight) for (weight,v) in self.graph[u]]

		distances = [[float("inf")]*self.size]
		distances[0][source] = 0

		for i in range(self.size - 1):
			temp = distances[-1].copy()
			for u, v, wt in edges:
				if distances[-1][u] == float("inf"):
					continue
				if temp[v] > distances[-1][u] + wt:
					temp[v] = distances[-1][u] + wt

			distances.append(temp)

		return distances

